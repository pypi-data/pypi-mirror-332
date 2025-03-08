# SPDX-FileCopyrightText: Copyright (c) 2024-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
from functools import partial

import jax
import jax.core
import jax.extend
import jax.lax
import jax.numpy as jnp
from jax.interpreters import ad, batching, mlir, xla

import cuequivariance as cue
from cuequivariance_jax.primitives.primitives_utils import reshape
from cuequivariance_jax.primitives.tensor_product_ops_impl import (
    tensor_product_ops_impl,
)
from cuequivariance_jax.primitives.tensor_product_vanilla_impl import (
    tensor_product_vanilla_impl,
)

logger = logging.getLogger(__name__)


def tensor_product(
    descriptors: list[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    inputs: list[jax.Array],
    outputs_shape_dtype: list[jax.ShapeDtypeStruct],
    indices: list[jax.Array | None] | None = None,
    *,
    math_dtype: jnp.dtype | None = None,
    name: str | None = None,
    impl: str = "auto",
) -> list[jax.Array]:
    r"""Compute a polynomial described by a list of descriptors.

    Features:
      - Calls a CUDA kernel if:
          - STPs have a single mode which is a multiple of 32 (e.g. a channelwise tensor product that has subscripts ``u,u,,u`` with u=128)
          - math data type is float32 or float64
          - in/out data type is a mix of float32, float64, float16 and bfloat16
          - indices are int32
      - Supports of infinite derivatives (JVP and tranpose rules maps to a single corresponding primitive)
      - Limited support for batching (we cannot batch a buffer that has indices and if the batching is non trivial the performace will be bad)
      - Automatic optimizations based on the symmetries of the STPs and on the repetition of the input buffers
      - Automatic drop of unused buffers and indices

    Args:
        descriptors (list of pairs): The list of descriptors.
            Each descriptor is formed by a pair of :class:`cue.Operation <cuequivariance.Operation>` and :class:`cue.SegmentedTensorProduct <cuequivariance.SegmentedTensorProduct>`.
        inputs (list of jax.Array): The input buffers.
        outputs_shape_dtype (list of jax.ShapeDtypeStruct): The output shapes and dtypes.
        indices (list of jax.Array or None, optional): The optional indices of the inputs and outputs.
        math_dtype (jnp.dtype, optional): The data type for computational operations. Defaults to None.
        name (str, optional): The name of the operation. Defaults to None.
        impl (str, optional): The implementation to use. Defaults to "auto".
            If "auto", it will use the CUDA implementation if available, otherwise it will use the JAX implementation.
            If "cuda", it will use the CUDA implementation.
            If "jax", it will use the JAX implementation.

    Returns:
        list of jax.Array: The result of the tensor product.
    """

    if name is None:
        name = "tensor_product"

    buffers = inputs + outputs_shape_dtype

    if indices is None:
        indices = [None] * len(buffers)

    if len(indices) != len(buffers):
        raise ValueError(
            f"Expected {len(buffers)} indices, got {len(indices)}. "
            "Please provide an index for each buffer. "
            "If a buffer does not have an index, please set it to None."
        )

    def fn(
        buffer: jax.Array | jax.ShapeDtypeStruct, idx: jax.Array | None
    ) -> jax.Array | jax.ShapeDtypeStruct:
        if buffer.ndim == 1 and idx is None:
            return reshape(buffer, (1, buffer.shape[0]))
        return buffer

    buffers = list(map(fn, buffers, indices))

    for i, buffer in enumerate(buffers):
        assert buffer.ndim == 2, (
            f"Expected buffer {i} to have 2 dimensions, got {buffer.shape}"
        )
    for i, idx in enumerate(indices):
        assert idx is None or idx.ndim == 1, (
            f"Expected index {i} to have 1 dimension, got {idx.shape}"
        )

    if math_dtype is None:
        math_dtype = jnp.result_type(*buffers)
        if math_dtype not in (jnp.float32, jnp.float64):
            math_dtype = jnp.float32

    assert math_dtype in (jnp.float32, jnp.float64), (
        f"math_dtype must be float32 or float64, got {math_dtype}"
    )

    buffer_index = []
    unique_indices = []
    for idx in indices:
        if idx is None:
            buffer_index.append(-1)
        else:
            found = False
            for j, uidx in enumerate(unique_indices):
                if idx is uidx:
                    buffer_index.append(j)
                    found = True
                    break
            if not found:
                buffer_index.append(len(unique_indices))
                unique_indices.append(idx)

    kwargs = dict(
        inputs=buffers[: len(inputs)],
        outputs_shape_dtype=buffers[len(inputs) :],
        indices=unique_indices,
        buffer_index=buffer_index,
        descriptors=descriptors,
        math_dtype=math_dtype,
        name=name,
    )

    if impl == "naive_jax":
        outputs = tensor_product_vanilla_impl(**kwargs)
    else:
        outputs = tensor_product_prim(**kwargs, impl=impl)

    def fn(x: jax.Array, shape: tuple[int, ...]) -> jax.Array:
        return jnp.reshape(x, shape)

    return list(map(fn, outputs, [out.shape for out in outputs_shape_dtype]))


tensor_product_p = jax.extend.core.Primitive("tensor_product")
tensor_product_p.multiple_results = True


def tensor_product_prim(
    inputs: list[jax.Array],  # input buffers
    outputs_shape_dtype: list[jax.ShapeDtypeStruct],  # output shapes and dtypes
    indices: list[jax.Array],  # index buffers
    buffer_index: list[int],  # maps: buffer index -> unique indices index
    descriptors: list[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    math_dtype: jnp.dtype,
    name: str,
    impl: str = "auto",
    return_none_if_empty: bool = False,
) -> tuple[jax.Array, ...]:  # output buffers
    """
    - Filters out unused buffers and indices
    - Calls the tensor product primitive
    - Maps the outputs back to the original output buffers
    """
    assert len(inputs) + len(outputs_shape_dtype) == len(buffer_index)
    assert max(buffer_index) < len(indices)

    descriptors = map(
        lambda x: (
            x[0],
            x[1].consolidate_modes().remove_empty_segments().consolidate_paths(),
        ),
        descriptors,
    )
    descriptors = list(filter(lambda x: x[1].num_paths > 0, descriptors))

    used_buffers = set()
    used_indices = set()
    for ope, _ in descriptors:
        for i in ope.buffers:
            used_buffers.add(i)
            if buffer_index[i] >= 0:
                used_indices.add(buffer_index[i])
    used_buffers = sorted(used_buffers)  # maps: new buffer index -> old buffer index
    used_indices = sorted(used_indices)  # maps: new index -> old index

    new_num_inputs = sum([i < len(inputs) for i in used_buffers])

    new_outputs = tensor_product_p.bind(
        *[inputs[i] for i in used_buffers[:new_num_inputs]],
        *[indices[i] for i in used_indices],
        buffer_index=tuple(
            used_indices.index(buffer_index[i]) if buffer_index[i] >= 0 else -1
            for i in used_buffers
        ),
        outputs_shape_dtype=tuple(
            outputs_shape_dtype[i - len(inputs)] for i in used_buffers[new_num_inputs:]
        ),
        descriptors=frozenset(
            [
                (cue.Operation([used_buffers.index(i) for i in ope.buffers]), stp)
                for ope, stp in descriptors
            ]
        ),
        math_dtype=jnp.dtype(math_dtype),
        name=str(name),
        impl=impl,
    )

    if return_none_if_empty:
        outputs = [None] * len(outputs_shape_dtype)
    else:
        outputs = [jnp.zeros(out.shape, out.dtype) for out in outputs_shape_dtype]

    for i, output in zip(used_buffers[new_num_inputs:], new_outputs):
        outputs[i - len(inputs)] = output

    return tuple(outputs)


def map_indices(
    old_indices: list[jax.Array], old_buffer_index: list[int], mapping: list[int]
) -> tuple[list[jax.Array], list[int]]:
    new_indices = []
    new_buffer_index = []

    for new_i, old_i in enumerate(mapping):
        if old_buffer_index[old_i] >= 0:
            idx = old_indices[old_buffer_index[old_i]]
            found = False
            for i, new_idx in enumerate(new_indices):
                if idx is new_idx:
                    new_buffer_index.append(i)
                    found = True
                    break
            if not found:
                new_buffer_index.append(len(new_indices))
                new_indices.append(idx)
        else:
            new_buffer_index.append(-1)
    return new_indices, new_buffer_index


def tensor_product_abstract_eval(
    *inputs_and_indices: jax.core.ShapedArray,
    buffer_index: tuple[int, ...],
    outputs_shape_dtype: tuple[jax.ShapeDtypeStruct, ...],
    descriptors: frozenset[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    math_dtype: jnp.dtype,
    name: str,
    impl: str,
) -> tuple[jax.core.ShapedArray, ...]:
    return tuple(
        jax.core.ShapedArray(out.shape, out.dtype) for out in outputs_shape_dtype
    )


def tensor_product_impl(
    platform: str | None,
    *inputs_and_indices: jax.Array,
    buffer_index: tuple[int, ...],
    outputs_shape_dtype: tuple[jax.ShapeDtypeStruct, ...],
    descriptors: frozenset[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    math_dtype: jnp.dtype,
    name: str,
    impl: str,
) -> tuple[jax.Array, ...]:
    num_inputs = len(buffer_index) - len(outputs_shape_dtype)
    inputs, indices = inputs_and_indices[:num_inputs], inputs_and_indices[num_inputs:]
    del inputs_and_indices

    def optimize_paths(ope: cue.Operation, stp: cue.SegmentedTensorProduct):
        for set_of_operands in ope.operands_with_identical_buffers():
            stp = stp.sort_indices_for_identical_operands(set_of_operands)
        stp = stp.sort_paths()
        return ope, stp

    descriptors = list(map(optimize_paths, *zip(*descriptors)))

    outputs = None
    kwargs = dict(
        inputs=inputs,
        outputs_shape_dtype=outputs_shape_dtype,
        indices=indices,
        buffer_index=buffer_index,
        descriptors=descriptors,
        math_dtype=math_dtype,
        name=name,
    )

    assert impl in ("auto", "cuda", "jax")

    if platform == "cuda" and impl in ("auto", "cuda"):
        outputs, msg = tensor_product_ops_impl(**kwargs)
    else:
        msg = f"{platform=}, {impl=}"

    if impl == "cuda" and outputs is None:
        raise RuntimeError(f"Failed to use CUDA implementation: {msg}")

    if outputs is None:
        outputs = tensor_product_vanilla_impl(**kwargs)

    assert outputs is not None
    return outputs


def tensor_product_jvp(
    primals_and_indices: tuple[jax.Array, ...],
    tangents_and_zeros: tuple[jax.Array | ad.Zero, ...],
    *,
    buffer_index: tuple[int, ...],
    outputs_shape_dtype: tuple[jax.ShapeDtypeStruct, ...],
    descriptors: frozenset[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    math_dtype: jnp.dtype,
    name: str,
    impl: str,
) -> tuple[tuple[jax.Array, ...], tuple[jax.Array | ad.Zero, ...]]:
    num_inputs = len(buffer_index) - len(outputs_shape_dtype)

    primals, tangents = (
        primals_and_indices[:num_inputs],
        tangents_and_zeros[:num_inputs],
    )
    indices = primals_and_indices[num_inputs:]
    assert all(isinstance(t, ad.Zero) for t in tangents_and_zeros[num_inputs:])
    del primals_and_indices, tangents_and_zeros

    out_primals = tensor_product_prim(
        primals,
        outputs_shape_dtype,
        indices,
        buffer_index,
        descriptors,
        math_dtype,
        name,
        impl=impl,
    )

    jvp_indices, jvp_buffer_index = map_indices(
        indices,
        buffer_index,
        [i for i, x in enumerate(primals)]
        + [i for i, x in enumerate(tangents) if not isinstance(x, ad.Zero)]
        + [num_inputs + i for i, x in enumerate(outputs_shape_dtype)],
    )

    jvp_descriptors = []
    for ope, stp in descriptors:
        jvps = ope.jvp([not isinstance(t, ad.Zero) for t in tangents])
        permutations: list[tuple[int, ...]] = stp.symmetries()
        for multiplicator, ope in cue.Operation.group_by_operational_symmetries(
            permutations, jvps
        ):
            jvp_descriptors.append((ope, multiplicator * stp))

    out_tangents = tensor_product_prim(
        list(primals) + [t for t in tangents if not isinstance(t, ad.Zero)],
        outputs_shape_dtype,
        jvp_indices,
        jvp_buffer_index,
        jvp_descriptors,
        math_dtype,
        name
        + "_jvp"
        + "".join("0" if isinstance(t, ad.Zero) else "1" for t in tangents),
        impl=impl,
    )

    return out_primals, out_tangents


def tensor_product_transpose(
    cotangents: tuple[jax.Array | ad.Zero, ...],
    *inputs_and_indices: jax.Array | ad.UndefinedPrimal,
    buffer_index: tuple[int, ...],
    outputs_shape_dtype: tuple[jax.ShapeDtypeStruct, ...],
    descriptors: frozenset[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    math_dtype: jnp.dtype,
    name: str,
    impl: str,
) -> tuple[jax.Array | ad.Zero | None, ...]:
    num_inputs = len(buffer_index) - len(outputs_shape_dtype)
    inputs, indices = inputs_and_indices[:num_inputs], inputs_and_indices[num_inputs:]
    assert all(not ad.is_undefined_primal(idx) for idx in indices)
    del inputs_and_indices

    # The cotangents replace the outputs as inputs
    # The undefined primal inputs become outputs

    tr_indices, tr_buffer_index = map_indices(
        indices,
        buffer_index,
        [i for i, x in enumerate(inputs) if not ad.is_undefined_primal(x)]
        + [
            num_inputs + i
            for i, x in enumerate(cotangents)
            if not isinstance(x, ad.Zero)
        ]
        + [i for i, x in enumerate(inputs) if ad.is_undefined_primal(x)],
    )

    tr_descriptors = []
    for ope, stp in descriptors:
        ope = ope.transpose(
            [ad.is_undefined_primal(x) for x in inputs],
            [not isinstance(x, ad.Zero) for x in cotangents],
        )
        if ope is not None:
            tr_descriptors.append((ope, stp))

    tmp = tensor_product_prim(
        [x for x in inputs if not ad.is_undefined_primal(x)]
        + [x for x in cotangents if not isinstance(x, ad.Zero)],  # inputs
        [
            jax.ShapeDtypeStruct(x.aval.shape, x.aval.dtype)
            for x in inputs
            if ad.is_undefined_primal(x)
        ],
        tr_indices,
        tr_buffer_index,
        tr_descriptors,
        math_dtype,
        name + "_transpose",
        impl=impl,
        return_none_if_empty=True,
    )

    outputs = [None] * (len(inputs) + len(indices))
    i = 0
    for b, input in enumerate(inputs):
        if ad.is_undefined_primal(input):
            outputs[b] = tmp[i] if tmp[i] is not None else ad.Zero(input.aval)
            i += 1
    return tuple(outputs)


def tensor_product_batching(
    batched_inputs_and_indices: tuple[jax.Array, ...],
    batch_axes_of_inputs_and_indices: tuple[int | None, ...],
    *,
    buffer_index: tuple[int, ...],
    outputs_shape_dtype: tuple[jax.ShapeDtypeStruct, ...],
    descriptors: frozenset[tuple[cue.Operation, cue.SegmentedTensorProduct]],
    math_dtype: jnp.dtype,
    name: str,
    impl: str,
) -> tuple[tuple[jax.Array, ...], tuple[int, ...]]:
    num_inputs = len(buffer_index) - len(outputs_shape_dtype)

    batched_inputs, batched_indices = (
        batched_inputs_and_indices[:num_inputs],
        batched_inputs_and_indices[num_inputs:],
    )
    del batched_inputs_and_indices
    batch_axes_of_inputs, batch_axes_of_indices = (
        batch_axes_of_inputs_and_indices[:num_inputs],
        batch_axes_of_inputs_and_indices[num_inputs:],
    )
    del batch_axes_of_inputs_and_indices

    for i in buffer_index[num_inputs:]:
        if i >= 0:
            raise ValueError("Batching is not supported when outputs have indices")
    for i, axis in zip(buffer_index[:num_inputs], batch_axes_of_inputs):
        if i >= 0 and axis is not None:
            raise ValueError("Batching is not supported for inputs that have indices")

    def prepare(input: jax.Array, axis: int | None) -> jax.Array:
        if axis is None:
            return jnp.expand_dims(input, 0)
        else:
            return jnp.moveaxis(input, axis, 0)

    batched_inputs = [
        input if i >= 0 else prepare(input, axis)
        for i, input, axis in zip(buffer_index, batched_inputs, batch_axes_of_inputs)
    ]
    batched_indices = [
        prepare(input, axis)
        for input, axis in zip(batched_indices, batch_axes_of_indices)
    ]

    # possible input buffer shapes:
    #  - (new_dim | 1, batch_size | 1, size)
    #  - (max_index, size)
    # possible indices shapes:
    #  - (new_dim | 1, batch_size)
    new_dim = 1
    batch_size = 1
    for x in batched_inputs:
        if x.ndim == 3:
            if x.shape[0] != 1:
                new_dim = x.shape[0]
            if x.shape[1] != 1:
                batch_size = x.shape[1]
    for x in batched_indices:
        if x.shape[0] != 1:
            new_dim = x.shape[0]
        if x.shape[1] != 1:
            batch_size = x.shape[1]

    def flatten_input(x: jax.Array) -> jax.Array:
        m, n, d = x.shape
        if (m, n) == (1, 1):
            return jnp.reshape(x, (1, d))
        x = jnp.broadcast_to(x, (new_dim, batch_size, d))
        return jnp.reshape(x, (new_dim * batch_size, d))

    batched_inputs = [flatten_input(x) if x.ndim == 3 else x for x in batched_inputs]

    def flatten_index(x: jax.Array) -> jax.Array:
        x = jnp.broadcast_to(x, (new_dim, batch_size))
        return jnp.reshape(x, (new_dim * batch_size))

    batched_indices = [flatten_index(x) for x in batched_indices]

    new_outputs_shape_dtype = tuple(
        jax.ShapeDtypeStruct((new_dim * batch_size, *out.shape[1:]), out.dtype)
        for out in outputs_shape_dtype
    )

    outputs = tensor_product_p.bind(
        *batched_inputs,
        *batched_indices,
        buffer_index=buffer_index,
        outputs_shape_dtype=new_outputs_shape_dtype,
        descriptors=descriptors,
        math_dtype=math_dtype,
        name=name + "_batching",
        impl=impl,
    )
    outputs = tuple(
        jnp.reshape(x, (new_dim, batch_size, *x.shape[1:])) for x in outputs
    )
    outputs = tuple(
        jnp.sum(x, axis=1, keepdims=True) if y.shape[0] == 1 else x
        for x, y in zip(outputs, outputs_shape_dtype)
    )
    return outputs, (0,) * len(outputs)


tensor_product_p.def_abstract_eval(tensor_product_abstract_eval)
tensor_product_p.def_impl(partial(xla.apply_primitive, tensor_product_p))
mlir.register_lowering(
    tensor_product_p,
    mlir.lower_fun(
        partial(tensor_product_impl, "cuda"), tensor_product_p.multiple_results
    ),
    "cuda",
)
mlir.register_lowering(
    tensor_product_p,
    mlir.lower_fun(
        partial(tensor_product_impl, None), tensor_product_p.multiple_results
    ),
    None,
)
ad.primitive_jvps[tensor_product_p] = tensor_product_jvp
ad.primitive_transposes[tensor_product_p] = tensor_product_transpose
batching.primitive_batchers[tensor_product_p] = tensor_product_batching

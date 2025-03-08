# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.
from __future__ import annotations

import ctypes
from enum import IntEnum
from typing import NamedTuple

import jax
import jax.numpy as jnp
import numpy as np
from jax import ffi

import cuequivariance_ops_jax._ext.cuequivariance_ops_jax_ext

library = ctypes.cdll.LoadLibrary(
    cuequivariance_ops_jax._ext.cuequivariance_ops_jax_ext.__file__
)
ffi.register_ffi_target(
    name="tensor_product_uniform_1d_jit",
    fn=ffi.pycapsule(getattr(library, "tensor_product_uniform_1d_jit")),
    platform="CUDA",
)


class BatchDimension(IntEnum):
    BATCHED = 0
    SHARED = 1
    INDEXED = 2


class SegmentDimension(IntEnum):
    SCALAR = 0
    VECTOR = 1


class DataType(IntEnum):
    FLOAT32 = 0
    FLOAT64 = 1
    FLOAT16 = 2
    BFLOAT16 = 3


def _batch_dim(
    buffer: jax.ShapeDtypeStruct, index: jax.ShapeDtypeStruct | None, batch_size: int
) -> BatchDimension:
    if index is None:
        if buffer.shape[0] == batch_size:
            return BatchDimension.BATCHED
        else:
            return BatchDimension.SHARED
    else:
        return BatchDimension.INDEXED


def _seg_dim(buffer: jax.ShapeDtypeStruct, operand_extent: int) -> SegmentDimension:
    if buffer.shape[2] == operand_extent:
        return SegmentDimension.VECTOR
    else:
        return SegmentDimension.SCALAR


def _dtype(jax_dtype: jnp.dtype) -> DataType:
    try:
        return {
            jnp.float32: DataType.FLOAT32,
            jnp.float64: DataType.FLOAT64,
            jnp.float16: DataType.FLOAT16,
            jnp.bfloat16: DataType.BFLOAT16,
        }[jnp.dtype(jax_dtype).type]
    except KeyError:
        raise ValueError(f"Unsupported dtype: {jax_dtype}")


class Operation(NamedTuple):
    buffers: list[int]
    start_path: int
    num_paths: int


class Path(NamedTuple):
    indices: list[int]
    coefficient: float


def _batch_size(
    buffers: list[jax.ShapeDtypeStruct],
    indices: list[jax.ShapeDtypeStruct | None],
) -> int:
    batch_size = 1
    for i, x in zip(indices, buffers):
        if i is None:
            bs = x.shape[0]
        else:
            bs = i.shape[0]
        if bs != 1:
            assert batch_size in {1, bs}
            batch_size = bs
    return batch_size


def _operand_extent(
    buffers: list[jax.ShapeDtypeStruct],
):
    operand_extent = max(x.shape[2] for x in buffers)
    for x in buffers:
        assert x.shape[2] in {1, operand_extent}, x.shape[2]
    return operand_extent


def _operation_start_indices(
    paths: list[Path], operation_start_paths: np.ndarray
) -> np.ndarray:
    path_num_operands = np.array([len(path.indices) for path in paths], dtype=np.int32)
    start_indices = np.append(0, np.cumsum(path_num_operands))
    return start_indices[operation_start_paths].astype(np.int64)


def tensor_product_uniform_1d_jit(
    input_buffers: list[jax.Array],
    output_buffers_shape_dtype: list[jax.ShapeDtypeStruct],
    unique_indices: list[jax.Array],
    buffer_index: list[int],  # -1 if not indexed
    *,
    operations: list[Operation],
    paths: list[Path],
    math_dtype: jnp.dtype,
    name: str = "untitled",
) -> list[jax.Array]:
    """JIT-compiled CUDA implementation of tensor_product_uniform_1d.

    Args:
        input_buffers: The input buffers. (batch_size or 1 or num_indices, num_segments, num_u or 1).
        output_buffers_shape_dtype: The shape and dtype of the output buffers. (batch_size or 1 or num_indices, num_segments, num_u or 1).
        unique_indices: The indices. (batch_size,)
        buffer_index: The buffer indices. -1 if not indexed.
        operations: The operations to perform.
        paths: The paths to use.
        math_dtype: The math dtype to use.
        name: The name of the operation.

    Returns:
        The output buffers.
    """
    io_buffers = input_buffers + output_buffers_shape_dtype

    assert len(buffer_index) == len(io_buffers)

    for x in io_buffers:
        assert x.ndim == 3

    for i in unique_indices:
        assert i.ndim == 1 and i.dtype == jnp.int32

    indices = [unique_indices[bi] if bi >= 0 else None for bi in buffer_index]
    batch_size = _batch_size(io_buffers, indices)
    operand_extent = _operand_extent(io_buffers)

    # TODO: remove this when atomic add is supported for float16 and bfloat16
    for i, b in zip(buffer_index[len(input_buffers) :], output_buffers_shape_dtype):
        if b.dtype.type not in {jnp.float32, jnp.float64}:
            if i >= 0 or b.shape[0] != batch_size:
                raise ValueError(
                    "Atomic add not supported for float16 or bfloat16 buffers"
                )

    math_dtype = jnp.dtype(math_dtype)
    assert math_dtype.type in {jnp.float32, jnp.float64}

    def ii(items):
        return np.array([i for i in items], dtype=np.int64)

    buffer_batch_dim = ii(
        _batch_dim(x, i, batch_size) for i, x in zip(indices, io_buffers)
    )
    buffer_num_segments = ii(x.shape[1] for x in io_buffers)
    buffer_segments_dim = ii(_seg_dim(x, operand_extent) for x in io_buffers)
    buffer_index = ii(buffer_index)
    buffer_dtype = ii(_dtype(x.dtype) for x in io_buffers)
    operation_num_operands = ii(len(op.buffers) for op in operations)
    operation_buffers = ii(b for op in operations for b in op.buffers)
    operation_num_paths = ii(op.num_paths for op in operations)
    operation_start_coeffs = ii(op.start_path for op in operations)
    operation_start_indices = _operation_start_indices(paths, operation_start_coeffs)
    path_indices = ii(i for path in paths for i in path.indices)
    path_coefficients = np.array([path.coefficient for path in paths], dtype=np.float64)

    call = ffi.ffi_call("tensor_product_uniform_1d_jit", output_buffers_shape_dtype)
    return call(
        *input_buffers,
        *unique_indices,
        name=name,
        math_dtype=_dtype(math_dtype),
        operand_extent=operand_extent,
        num_indices=len(unique_indices),
        buffer_batch_dim=buffer_batch_dim,
        buffer_num_segments=buffer_num_segments,
        buffer_segments_dim=buffer_segments_dim,
        buffer_index=buffer_index,
        buffer_dtype=buffer_dtype,
        operation_num_operands=operation_num_operands,
        operation_buffers=operation_buffers,
        operation_num_paths=operation_num_paths,
        operation_start_indices=operation_start_indices,
        operation_start_coeffs=operation_start_coeffs,
        path_indices=path_indices,
        path_coefficients=path_coefficients.view(np.int64),
        batch_size=batch_size,
    )

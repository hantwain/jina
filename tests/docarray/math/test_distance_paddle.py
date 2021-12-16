import numpy as np
import pytest
import paddle

from docarray.math.distance.numpy import (
    cosine as cosine_numpy,
    sqeuclidean as sqe_numpy,
)
from docarray.math.distance.paddle import cosine as cosine_paddle
from docarray.math.distance.paddle import sqeuclidean as sqe_paddle


@pytest.fixture
def get_a_b():
    a = np.random.random([7, 100])
    b = np.random.random([9, 100])
    yield a, b


def test_cosine(get_a_b):
    a, b = get_a_b
    r_torch = cosine_paddle(paddle.Tensor(a), paddle.Tensor(b))
    r_numpy = cosine_numpy(a, b)
    np.testing.assert_almost_equal(r_torch, r_numpy)


def test_sqeuclidean(get_a_b):
    a, b = get_a_b
    r_torch = sqe_paddle(paddle.Tensor(a), paddle.Tensor(b))
    r_numpy = sqe_numpy(a, b)
    np.testing.assert_almost_equal(r_torch, r_numpy)
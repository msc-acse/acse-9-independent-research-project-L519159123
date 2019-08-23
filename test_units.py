# Author: Yuxuan Liu
# Github Alias: L519159123

"""This module contains functions relating to the units testing of the software
"""

import sys

sys.path.append(".")

from util.util import *
import pytest
import numpy as np

def test_valid_print_numpy():
    x = np.array([1, 2, 0, 1, 3, 5])
    x_min, x_max, x_mean, x_median = print_numpy(x)
    assert x_min == 0
    assert x_max == 5

def test_invalid_print_numpy():
    x = np.array([[1, 2, 3], [2, -1, -1]])
    x_min, x_max, x_mean, x_median = print_numpy(x)
    assert not x_mean == 0
    assert not x_median == 2

def test_valid_tensor2im():
    x = torch.rand(1, 1, 128, 128)
    y = tensor2im(x)
    assert isinstance(y, np.ndarray)

def test_invalid_tensor2im():
    x = np.random.rand(32, 32)
    y = tensor2im(x)
    assert not y.shape == (3, 32, 32)

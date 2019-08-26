"""
author : Yuxuan Liu
github alias: L519159123
"""

"""This module contains functions relating to the units testing of the software
"""

import sys

sys.path.append(".")

from util.util import *
from data.base_dataset import *
from data.image_folder import *
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

def test_valid_crop():
    x = np.random.rand(32, 32)
    y = crop(x, 5, 5)
    assert y.shape == (5, 5)

def test_invalid_crop():
    x = np.random.rand(32, 32)
    y = crop(x, 35, 35)
    assert not y.shape == (35, 35)

def test_valid_scale_width():
    x = np.random.rand(32, 32)
    y = scale_width(x, 32)
    assert y.shape == (32, 32)

def test_valid_data_file():
    x = 'datafile.txt'
    y = is_data_file(x)
    assert y == 1

def test_invalid_data_file():
    x = 'datafile.png'
    y = is_data_file(x)
    assert y == 0


from decimal import Decimal
import numpy as np
import pytest

from matrixfmt import format_matrix



def test_array_of_ints():
    array = np.array([[1, 2], [3, 4]])
    expected = "\\begin{pmatrix}\n1 & 2\\\\\n3 & 4\n\\end{pmatrix}"

    assert format_matrix(array) == expected



def test_array_of_floats():
    array = np.array([[1., 2.], [3., 4.]])
    expected = "\\begin{pmatrix}\n1.0 & 2.0\\\\\n3.0 & 4.0\n\\end{pmatrix}"

    assert format_matrix(array) == expected


def test_array_of_decimals():
    inner = [[Decimal(1), Decimal(2)], [Decimal(3), Decimal(4)]]
    array = np.array(inner)
    expected = "\\begin{pmatrix}\n1 & 2\\\\\n3 & 4\n\\end{pmatrix}"

    assert format_matrix(array) == expected


def test_array_of_row_vector():
    array = np.array([[1., 2., 3., 4.]])
    expected = "\\begin{pmatrix}\n1.0 & 2.0 & 3.0 & 4.0\n\\end{pmatrix}"

    assert format_matrix(array) == expected


def test_array_of_column_vector():
    array = np.array([[1.], [2.], [3.], [4.]])
    expected = "\\begin{pmatrix}\n1.0\\\\\n2.0\\\\\n3.0\\\\\n4.0\n\\end{pmatrix}"

    assert format_matrix(array) == expected


def test_array_of_floats():
    array = np.array([[1., 2.], [3., 4.]])
    expected = "\\begin{pmatrix}\n1.0 & 2.0\\\\\n3.0 & 4.0\n\\end{pmatrix}"

    assert format_matrix(array) == expected


def test_1_dimensional_array():
    array = np.array([1, 2, 3, 4])
    expected = "\\begin{pmatrix}\n1 & 2 & 3 & 4\n\\end{pmatrix}"

    assert format_matrix(array) == expected




from typing import List


class Mat2D:
    def __init__(self, data: List[List[float]]):
        if len(data) != 2 or len(data[0]) != 2 or len(data[1]) != 2:
            raise ValueError("Mat2D must be a 2x2 matrix")
        self.data = data


def add(m1: Mat2D, m2: Mat2D) -> Mat2D:
    """
    Adds two 2x2 matrices.

    :param m1: First matrix
    :param m2: Second matrix
    :return: The sum of the two matrices
    """
    return Mat2D(
        [
            [m1.data[0][0] + m2.data[0][0], m1.data[0][1] + m2.data[0][1]],
            [m1.data[1][0] + m2.data[1][0], m1.data[1][1] + m2.data[1][1]],
        ]
    )


def subtract(m1: Mat2D, m2: Mat2D) -> Mat2D:
    """
    Subtracts another 2x2 matrix from the first matrix.

    :param m1: First matrix
    :param m2: Second matrix
    :return: The difference of the two matrices
    """
    return Mat2D(
        [
            [m1.data[0][0] - m2.data[0][0], m1.data[0][1] - m2.data[0][1]],
            [m1.data[1][0] - m2.data[1][0], m1.data[1][1] - m2.data[1][1]],
        ]
    )


def multiply(m1: Mat2D, m2: Mat2D) -> Mat2D:
    """
    Multiplies two 2x2 matrices.

    :param m1: First matrix
    :param m2: Second matrix
    :return: The product of the two matrices
    """
    return Mat2D(
        [
            [
                m1.data[0][0] * m2.data[0][0] + m1.data[0][1] * m2.data[1][0],
                m1.data[0][0] * m2.data[0][1] + m1.data[0][1] * m2.data[1][1],
            ],
            [
                m1.data[1][0] * m2.data[0][0] + m1.data[1][1] * m2.data[1][0],
                m1.data[1][0] * m2.data[0][1] + m1.data[1][1] * m2.data[1][1],
            ],
        ]
    )


def determinant(mat: Mat2D) -> float:
    """
    Calculates the determinant of the 2x2 matrix.

    :param mat: The matrix
    :return: The determinant of the matrix
    """
    return mat.data[0][0] * mat.data[1][1] - mat.data[0][1] * mat.data[1][0]


def transpose(matrix: Mat2D) -> Mat2D:
    """
    Transposes the 2x2 matrix.

    :param matrix: The matrix
    :return: The transposed matrix
    """
    return Mat2D(
        [
            [matrix.data[0][0], matrix.data[1][0]],
            [matrix.data[0][1], matrix.data[1][1]],
        ]
    )

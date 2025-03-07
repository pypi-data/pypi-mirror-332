from typing import List


class Mat3D:
    def __init__(self, data: List[List[float]]):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Mat3D must be a 3x3 matrix")
        self.data = data


def add(m1: Mat3D, m2: Mat3D) -> Mat3D:
    """
    Adds two 3x3 matrices.

    :param m1: First matrix
    :param m2: Second matrix
    :return: The sum of the two matrices
    """
    return Mat3D(
        [[m1.data[i][j] + m2.data[i][j] for j in range(3)] for i in range(3)]
    )


def subtract(m1: Mat3D, m2: Mat3D) -> Mat3D:
    """
    Subtracts another 3x3 matrix from the first matrix.

    :param m1: First matrix
    :param m2: Second matrix
    :return: The difference of the two matrices
    """
    return Mat3D(
        [[m1.data[i][j] - m2.data[i][j] for j in range(3)] for i in range(3)]
    )


def multiply(m1: Mat3D, m2: Mat3D) -> Mat3D:
    """
    Multiplies two 3x3 matrices.

    :param m1: First matrix
    :param m2: Second matrix
    :return: The product of the two matrices
    """
    return Mat3D(
        [
            [
                sum(m1.data[i][k] * m2.data[k][j] for k in range(3))
                for j in range(3)
            ]
            for i in range(3)
        ]
    )


def determinant(matrix: Mat3D) -> float:
    """
    Calculates the determinant of the 3x3 matrix.

    :param matrix: The matrix
    :return: The determinant of the matrix
    """
    a, b, c = matrix.data[0]
    d, e, f = matrix.data[1]
    g, h, i = matrix.data[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def transpose(matrix: Mat3D) -> Mat3D:
    """
    Transposes the 3x3 matrix.

    :param matrix: The matrix
    :return: The transposed matrix
    """
    return Mat3D([[matrix.data[j][i] for j in range(3)] for i in range(3)])

"""
    Vector(list=[]) -> create Vector object
"""

import numpy as np


class Vector:

    """
    __init__(...)
    solve(...)
    __str__()
    arr
    """
    def __init__(self, *array):
        """

        Vector initialization

        :param array - that stores vector elements:
        """
        self.arr = np.array(array)

    def solve(self, matrix):
        """

        return solution of matrix equation
        :param matrix:
        :return Vector:
        """
        try:
            return Vector(*np.linalg.solve(np.array([v.arr for v in matrix.arr]), self.arr))
        except np.linalg.LinAlgError:
            print('bad matrix')

    def __str__(self):
        """

        return string representation of object
        :return str(Vector.arr):
        """
        return str(self.arr)

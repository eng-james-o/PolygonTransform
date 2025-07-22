from math import sin, cos, radians as rad


def _matric_multiplication(mat, T_mat):
    transform_matrix = []
    for i in range(len(mat)):
        transform_matrix.append([0, 0, 0])

    for i in range(len(mat)):
        for j in range(len(T_mat[0])):
            for k in range(len(T_mat)):
                transform_matrix[i][j] += mat[i][k] * T_mat[k][j]
    return transform_matrix


class Transformation:

    def __init__(self, points):
        self.matrix = points
        self._matrix = points
        self.result = []

    def translate(self, tx, ty):
        translational_matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [tx, ty, 1]
        ]
        self.result = _matric_multiplication(self._matrix, translational_matrix)
        self._set_result()
        return self.result

    def rotate(self, angle, delimiter='CLOCKWISE'):
        if delimiter.casefold() == 'CLOCKWISE'.casefold():
            sense = 1
        elif delimiter.casefold() == 'ANTICLOCKWISE'.casefold():
            sense = -1
        else:
            raise TypeError(f'Unknown delimiter value "{delimiter}"')

        angle = rad(angle)
        rotational_matrix = [
            [cos(angle),         -sense * sin(angle), 0],
            [sense * sin(angle), cos(angle),          0],
            [0,                  0,                   1]
        ]
        self.result = _matric_multiplication(self._matrix, rotational_matrix)
        self._set_result()
        return self.result

    def scale(self, sx, sy):
        scaling_matrix = [
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ]
        self.result = _matric_multiplication(self._matrix, scaling_matrix)
        self._set_result()
        return self.result

    def _set_result(self):
        self._matrix = self.result


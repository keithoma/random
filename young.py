from numpy import Infinity

import numpy as np

INF = 999999999 # very big number

def delete_minimal(_mat):
    n = len(_mat)
    m = len(_mat[0])

    def sort_recursively(i, j):
        if i + 1 >= n and j + 1 >= m:
            return _mat
        if not i + 1 >= n:
            if _mat[i + 1][j] >= _mat[i][j + 1]:
                _mat[i][j] = _mat[i + 1][j]
                _mat[i + 1][j] = INF
                return sort_recursively(i + 1, j)
        else:
            _mat[i][j] = _mat[i][j + 1]
            _mat[i][j + 1] = INF
            return sort_recursively(i, j + 1)

    _mat[0][0] = INF
    return sort_recursively(0, 0)

def main():
    mat = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print(delete_minimal(mat))

if __name__ == "__main__":
    main()
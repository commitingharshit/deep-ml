def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    """
    def det(m):
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    d = det(matrix)
    if d == 0:
        return None

    a, b = matrix[0]
    c, e = matrix[1]

    inverse = [
        [e/d, -b/d],
        [-c/d, a/d]
    ]

    return inverse 

    """ Unique way of writing code, didnt know this
    """

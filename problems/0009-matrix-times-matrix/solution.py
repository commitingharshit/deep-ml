def matrixmul(a: list[list[int|float]],
              b: list[list[int|float]]) -> list[list[int|float]]:
    row_a, col_a = len(a), len(a[0])
    row_b, col_b = len(b), len(b[0])

    if col_a != row_b:
        return -1   # instead of raising ValueError

    res = [[0 for _ in range(col_b)] for _ in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                res[i][j] += a[i][k] * b[k][j]

    return res
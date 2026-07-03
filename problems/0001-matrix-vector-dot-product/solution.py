def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    res = []

    for row in a:
        if len(row) != len(b):
            return -1
        dot = sum(row[i] * b[i] for i in range(len(b)))
        res.append(dot)

    return res
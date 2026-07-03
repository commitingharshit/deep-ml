def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    """
    transpose = [[0 for j in range(len(a))] for i in range(len(a[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            transpose[j][i] = a[i][j]
    return transpose
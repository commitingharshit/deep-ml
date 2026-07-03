import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    def mean_by_row(matrix):
        means = []
        for row in matrix:
            means.append(sum(row) / len(row))
        return means

    if mode == "row":
        return mean_by_row(matrix)
    else:
        return mean_by_row(np.transpose(matrix))
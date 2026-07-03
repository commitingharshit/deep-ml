import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A_np = np.array(A)
    T_np = np.array(T)
    S_np = np.array(S)

    if np.linalg.det(T_np) == 0 or np.linalg.det(S_np) == 0:
        return -1

    T_inv = np.linalg.inv(T_np)
    transformed_matrix = T_inv @ A_np @ S_np

    return transformed_matrix.tolist()
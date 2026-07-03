def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    # Manual method for a 2x2 matrix using trace and determinant:
    # eigenvalues = (t ± sqrt(t^2 - 4d)) / 2
    t = matrix[0][0] + matrix[1][1]                              # trace
    d = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]    # determinant

    discriminant = t**2 - 4*d
    sqrt_disc = discriminant**0.5   # works for real eigenvalues (discriminant >= 0)

    eigen1 = (t + sqrt_disc) / 2
    eigen2 = (t - sqrt_disc) / 2

    eigenvalues = [eigen1, eigen2]
    return eigenvalues


# ---- Using numpy ----
# import numpy as np
# def calculate_eigenvalues_numpy(matrix):
#     values, vectors = np.linalg.eig(np.array(matrix))
#     return values.tolist()

# ---- Using torch ----
# import torch
# def calculate_eigenvalues_torch(matrix):
#     t = torch.tensor(matrix, dtype=torch.float32)
#     values = torch.linalg.eigvals(t)   # returns complex tensor
#     return values.tolist()
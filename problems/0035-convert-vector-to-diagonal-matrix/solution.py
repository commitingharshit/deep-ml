import numpy as np

def make_diagonal(x):
    n = len(x)
    res = []

    for i in range(n):
        row = [0] * n
        row[i] = x[i]
        res.append(row)

    return res
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    X = np.array(X)

    if y is not None:
        y = np.array(y)

    n_samples = len(X)
    batches = []

    for start in range(0, n_samples, batch_size):
        end = start + batch_size

        if y is None:
            batches.append(X[start:end])
        else:
            batches.append((X[start:end], y[start:end]))

    return batches
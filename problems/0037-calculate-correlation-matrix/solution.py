import numpy as np

def calculate_correlation_matrix(X, Y=None):

    if Y is None:
        return np.corrcoef(X, rowvar=False)

    n_x = X.shape[1]

    combined = np.hstack((X, Y))

    corr = np.corrcoef(combined, rowvar=False)

    return corr[:n_x, n_x:]
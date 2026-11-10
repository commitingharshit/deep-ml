import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    # Your code here
    n = len(X) 

    if replacements:
        subset_size = n
    else:
        subset_size = n//2  

    result = []

    for _ in range(n_subsets):

        indices = np.random.choice(n, subset_size, replace=replacements)

        X_subset = X[indices]
        y_subset = y[indices]

        result.append((X_subset.tolist(), y_subset.tolist())) 

    return result
    
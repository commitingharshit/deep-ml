import numpy as np

def gradient_descent(X, y, weights, learning_rate,
                     n_epochs, batch_size=1, method='batch'):

    n = len(y)
    weights = weights.copy()

    if method == 'batch':
        batch_size = n

    elif method == 'stochastic':
        batch_size = 1

    elif method == 'mini_batch':
        pass

    else:
        raise ValueError("Invalid method")

    for epoch in range(n_epochs):

        for i in range(0, n, batch_size):

            X_batch = X[i:i + batch_size]
            y_batch = y[i:i + batch_size]

            y_pred = X_batch @ weights

            error = y_pred - y_batch

            gradient = (2 / len(y_batch)) * (X_batch.T @ error)

            weights -= learning_rate * gradient

    return weights
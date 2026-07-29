import numpy as np

def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int
):

    weights = initial_weights.astype(float).copy()
    bias = float(initial_bias)

    mse_values = []

    n_samples = len(features)

    for _ in range(epochs):

        # Forward pass
        z = np.dot(features, weights) + bias
        predictions = 1 / (1 + np.exp(-z))

        # Loss
        mse = np.mean((labels - predictions) ** 2)
        mse_values.append(round(float(mse), 4))

        # Backpropagation
        dL_dyhat = 2 * (predictions - labels)
        dyhat_dz = predictions * (1 - predictions)
        dL_dz = dL_dyhat * dyhat_dz

        # Average gradients
        gradient_weights = np.dot(features.T, dL_dz) / n_samples
        gradient_bias = np.mean(dL_dz)

        # Gradient descent
        weights -= learning_rate * gradient_weights
        bias -= learning_rate * gradient_bias

    updated_weights = np.round(weights, 4)
    updated_bias = round(float(bias), 4)

    return updated_weights, updated_bias, mse_values
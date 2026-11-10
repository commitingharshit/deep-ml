import numpy as np

def polynomial_features(X, degree):
    result = []

    for row in X:
        features = [1]  # FIX: Include constant feature

        def generate(start, depth, product):
            if depth == 0:
                features.append(product)
                return

            for i in range(start, len(row)):
                generate(i, depth - 1, product * row[i])

        for d in range(1, degree + 1):
            generate(0, d, 1)

        result.append(sorted(features))

    return np.array(result, dtype=float)
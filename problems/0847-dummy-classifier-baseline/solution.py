import numpy as np
from collections import Counter 
import math

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    classes = sorted(set(y_train)) 

    if strategy == "most_frequent": 
        counts = Counter(y_train) 

        majority = min(classes, key=lambda c: (-counts[c], c))

        return [majority]*n_test
         
    elif strategy == "constant": 
        return [constant]*n_test

    elif strategy == "uniform": 
        k = len(classes) 

        return [classes[i%k] for i in range(n_test)]

    elif strategy == "stratified":
        counts = Counter(y_train)
        n = len(y_train)

        exact = [n_test * counts[c] / n for c in classes]
        allocated = [math.floor(v) for v in exact]

        remaining = n_test - sum(allocated)

        order = sorted(
            range(len(classes)),
            key=lambda i: (-(exact[i] - allocated[i]), classes[i])
        )

        for i in order[:remaining]:
            allocated[i] += 1

        result = []

        for c, count in zip(classes, allocated):
            result.extend([c] * count)

        return result
    else:
        raise("ValueError")


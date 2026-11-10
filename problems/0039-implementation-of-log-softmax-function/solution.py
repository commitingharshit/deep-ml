import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    # Your code here
    scores = np.array(scores, dtype = float)

    shifted = scores - np.max(scores)

    log_sum = np.log(np.sum(np.exp(shifted)))

    return shifted - log_sum
import numpy as np

def divide_on_feature(X, feature_i, threshold):

    condition = X[:, feature_i] >= threshold

    group_1 = X[condition]
    group_2 = X[~condition]

    return [group_1, group_2]
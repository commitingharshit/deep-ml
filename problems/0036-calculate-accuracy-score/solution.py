import numpy as np
def accuracy_score(y_true, y_pred):
    if len(y_true) != len(y_pred):
        return -1

     

    TP, FP, FN, TN = 0, 0, 0, 0

    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            TP += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            FN += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            FP += 1
        else:
            TN += 1

    return (TP + TN) / (TP + FP + FN + TN)
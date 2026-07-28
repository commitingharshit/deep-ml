import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    exp_scores = [math.exp(score-max_score) for score in scores] 
    max_score = max(scores)

    
    total = sum(exp_scores)

    return [value/total for value in exp_scores]


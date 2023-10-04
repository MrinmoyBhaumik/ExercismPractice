def latest(scores):
    last = len(scores) - 1
    return scores[last]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores = []
    for i in range(len(scores)):
        top_scores.append(max(scores))
        scores.remove(max(scores))
        if len(top_scores) > 2:
            break
    return top_scores


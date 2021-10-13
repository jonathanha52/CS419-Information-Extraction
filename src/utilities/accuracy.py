def precision(R, list_relevant):
    count = 0
    for doc in list_relevant:
        if doc in R:
            count += 1
    return count/len(list_relevant)


def recall(R, list_relevant):
    count = 0
    for doc in list_relevant:
        if doc in R:
            count += 1
    return count/len(R)


def f1_score(R, list_relevant):
    P = precision(R, list_relevant)
    r = recall(R, list_relevant)
    return 2*P*r / (P+r)

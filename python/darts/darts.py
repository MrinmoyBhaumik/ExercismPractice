def score(x, y):
    dist = (x**2 + y**2)**.5
    print (dist)
    if dist > 10:
        return 0
    if 5 < dist <= 10 :
        return 1
    if 1 < dist <= 5:
        return 5
    return 10
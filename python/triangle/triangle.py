def equilateral(sides):
    if (sides[0] == sides[1] == sides[2]) and (sides[0] != 0):
        return True
    return False


def isosceles(sides):
    double = 0
    single = 0
    for side in sides:
        if sides.count(side) == 1 and single == 0:
            single += side
        if sides.count(side) == 2 and double == 0:
            double += side
        if sides.count(side) == 3 and side != 0:
            return True
    if (double >0) and (2*double >= single):
        return True
    return False


def scalene(sides):
    for side in sides:
        if sides.count(side) > 1:
            return False
    if (sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0]):
       return True
    return False

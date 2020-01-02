import math


def giniIndex(total, inClassA, inClassB):
    # Returns the gini index
    if total == 0:
        return 1
    gini = 1 - ((inClassA / total) ** 2 + (inClassB / total) ** 2)
    if 0 <= gini <= 1:
        return gini
    else:
        print("Gini index problem")
        return 0


def determineLabels(array):
    # Finds the different labels of an attribute
    seen = []
    for label in array:
        if len(label) != 3:
            print("Invalid value detected")
        there = False
        for s in seen:
            if s == label[1]:
                there = True
        if not there:
            seen.append(label[1])
    return seen


def initialCounter(data, classes, columns):
    # Creates the initial counter of a node, called n in psuedocode
    n = {}
    for c in classes:
        per_class = {}
        for col in columns:
            per_column = {}
            labels = determineLabels(data[col])
            for l in labels:
                per_column[l] = 0
            per_class[col] = per_column
        n[c] = per_class
    return n


def updateBestGini(best, second_best, new):
    # Sets best to the lowest gini out of the three arguments and sets second_best to the second to lowest gini
    if new[0] < best[0]:
        return new, best
    if new[0] < second_best[0]:
        return best, new
    else:
        return best, second_best


def epsilon(n, R, delta):
    # Calculates the value for epsilon, explanation in report
    return math.sqrt(pow(R, 2) * math.log1p(1 / delta) / 2 * n)

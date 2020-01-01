from itertools import combinations
from math import ceil
import math


def giniIndex(total, inClassA, inClassB):
    if total == 0:
        return 0            #TODO not sure if this is a good choice
    gini = 1 - ((inClassA / total) ** 2 + (inClassB / total) ** 2)
    if 0 <= gini <= 1:
        return gini
    else:
        print("Gini index problem")
        return 0


def determineLabels(array):  # Finds the different classes of an attribute
    seen = []

    for label in array:
        there = False
        for s in seen:
            if s == label[1]:
                there = True
        if not there:
            seen.append(label[1])
    return seen


def initialCounter(data, classes, columns):
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
    if new[0] < best[0]:
        return new, best
    if new[0] < second_best[0]:
        return best, new
    else:
        return best, second_best


# TODO test this
def epsilon(n, R, delta):
    return math.sqrt(pow(R, 2) * math.log1p(1 / delta) / 2 * n)

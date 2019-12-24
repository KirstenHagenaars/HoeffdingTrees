from itertools import combinations
from math import ceil
import math


def giniIndex(total, inClassA, inClassB):
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


# TODO test/fix this function, it works for odd numbers of labels, there are duplicates when the nr of labels is even
def allSplits(labels):
    combis = []
    # when the labels are ['x', 'b', 's', 'f'], we do not want [['x', 'b', 's', 'f'],[]] in combis since this is not a split, right?
    for i in range(1, ceil((len(labels) + 1) / 2)):
        comb = combinations(labels, i)
        for j in comb:
            combine = [list(j)]
            print(j)
            partB = []
            for label in labels:
                seen = False
                for p in j:
                    if p == label:
                        seen = True
                if not seen:
                    partB.append(label)
            combine.append(partB)
            combis.append(combine)
    return combis


def countInstances2(instances, attribute, labels):  # Counts the number of instances of diff.classes within an attribute
    counted = [0 for x in range(0, len(labels))]

    for i in range(0, len(instances)):
        for label in labels:
            index = labels.index(label)
            if instances.iloc[i][attribute][1] == label:
                counted[index] = counted[index] + 1
                break
    return counted


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

import pandas as pd
from itertools import combinations
from math import ceil
import math
import numpy as np
import HTree

data = None
classes = []


def loadData():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")  # panda dataframe


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


def countInstances(instances, attribute, labels):  # Counts the number of instances of diff.classes within an attribute
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


def epsilon(n, R, delta):
    return math.sqrt(pow(R, 2) * math.log1p(1 / delta) / 2 * n)


# TODO finish function
def impurity(instances, labels):  # labels off 'class', found in the main

    # Find number of instances of each class
    counted = countInstances(instances, "class", labels)

    # Compute current gini index
    currentGini = giniIndex(len(instances), counted[0], counted[1])                             #line 3 psuedocode
    if (currentGini != 0):                                                                      # line 15 of psuedocode, gini = 0 if all instances are of the same class
        # Test all possible splits
        best, second_best = [1, None], [1, None]  # first element is the gini, second element is the corresponding split
        for attribute in instances.columns:
            labels = determineLabels(instances[attribute])
            splits = allSplits(labels)
            for split in splits:
                counted = countInstances(instances, "class", labels)  # TODO: change arguments
                gini = giniIndex(len(instances), counted[0],
                                 counted[1])  # not sure if these are the correct arguments?
                best, second_best = updateBestGini(best, second_best, [gini, split])
        best, second_best = updateBestGini(best, second_best, [currentGini, None])
        print(best)
        # Weight branch impurity by empirical branch probability for every possible split
        # if (best[1] != None and best[0]-second_best[0]>epsilon(len(instances), range, delta)): #line 20 of pseudocode


def main():
    loadData()
    global data
    class_labels = data["class"]
    global classes
    classes = determineLabels(class_labels)
    print(classes)

    classA = classes[0]
    classB = classes[1]

    # TEST CODE -------------------------
    test = data.iloc[range(0, 20)]
    # print(test)
    # print(test.shape)

    print("determineLabels")
    labels = determineLabels(test["cap-shape"])
    print(labels)
    print("instances")
    instances = countInstances(test, "cap-shape", labels)
    print(instances)

    #I start following the pseudocode from here:
    n = []
    for c in classes:
        per_class = []
        for col in data.columns:
            per_column = []
            labels = determineLabels(test[col])
            for l in labels:
                per_column.append(0)
            per_class.append(per_column)
        n.append(per_class)
    HT = HTree.Tree(n)
    for instance in test:
        HT.process(instance, classes, data.columns)

    # Something funky going on here
    # print(allSplits(labels))

    # print(allSplits(['a', 'b', 'c', 'd']))

    # --------------------------------------

    # TODO Change input! range(0, 10) just for testing purposes
    #impurity(data.iloc[range(0, 10)], classes)

main()

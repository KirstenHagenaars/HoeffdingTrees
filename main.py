import pandas as pd
from itertools import combinations
from math import ceil
import math
import numpy as np
import HTree
import Util

data = None
classes = []


def loadData():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")  # panda dataframe


# TODO finish function
def impurity(instances, labels):  # labels off 'class', found in the main

    # Find number of instances of each class
    counted = Util.countInstances(instances, "class", labels)

    # Compute current gini index
    currentGini = Util.giniIndex(len(instances), counted[0], counted[1])  # line 3 psuedocode
    if (currentGini != 0):  # line 15 of psuedocode, gini = 0 if all instances are of the same class
        # Test all possible splits
        best, second_best = [1, None], [1, None]  # first element is the gini, second element is the corresponding split
        for attribute in instances.columns:
            labels = Util.determineLabels(instances[attribute])
            splits = Util.allSplits(labels)
            for split in splits:
                counted = Util.countInstances(instances, "class", labels)  # TODO: change arguments
                gini = Util.giniIndex(len(instances), counted[0],
                                 counted[1])  # not sure if these are the correct arguments?
                best, second_best = Util.updateBestGini(best, second_best, [gini, split])
        best, second_best = Util.updateBestGini(best, second_best, [currentGini, None])
        print(best)
        # Weight branch impurity by empirical branch probability for every possible split
        # if (best[1] != None and best[0]-second_best[0]>epsilon(len(instances), range, delta)): #line 20 of pseudocode


def main():
    loadData()
    global data
    class_labels = data["class"]
    global classes
    classes = Util.determineLabels(class_labels)
    print(classes)

    classA = classes[0]
    classB = classes[1]

    # TEST CODE -------------------------
    test = data.iloc[range(0, 20)]
    # print(test)
    # print(test.shape)

    print("determineLabels")
    labels = Util.determineLabels(test["cap-shape"])
    print(labels)
    print("instances")
    instances = Util.countInstances(test, "cap-shape", labels)
    print(instances)

    # I start following the pseudocode from here:
    n = []
    for c in classes:
        per_class = []
        for col in data.columns:
            per_column = []
            labels = Util.determineLabels(test[col])
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
    # impurity(data.iloc[range(0, 10)], classes)


main()

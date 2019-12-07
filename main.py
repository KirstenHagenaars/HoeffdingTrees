import pandas as pd
from itertools import combinations
from math import ceil
import numpy as np
import HTree

data = None
classes = []


def load_data():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")  # panda dataframe
    # print(data.head())


def gini_index(total, inClassA, inClassB):
    gini = 1 - ((inClassA / total) ** 2 + (inClassB / total) ** 2)
    if 0 <= gini <= 1:
        return gini
    else:
        print("Gini index problem")
        return 0


def determineLabels(array):  # Finds the different classes of an attribute
    #labels = []
    seen = []

    for label in array:
        there = False
        for s in seen:
            if s == label[1]:
                there = True
        if not there:
            #labels.append(label[1])
            seen.append(label[1])
    return seen #labels

# TODO test/fix this function, it works for odd numbers of labels, there are duplicates when the nr of labels is even
def allSplits(labels):
    combis = []
    #when the labels are ['x', 'b', 's', 'f'], we do not want [['x', 'b', 's', 'f'],[]] in combis since this is not a split, right?
    for i in range(1, ceil((len(labels) + 1)/2)):
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


# TODO finish function
def impurity(instances, labels):    #labels off 'class', found in the main

    # TODO use countInstances here
    # Find number of instances of each class
    counted = countInstances(instances, "class", labels)

    # Compute gini index
    gini = gini_index(len(instances), counted[0], counted[1])

    # Test all possible splits

    for attribute in instances.columns:
        labels = determineLabels(instances[attribute])

    # Weight branch impurity by empirical branch probability for every possible split
    # CODE...


def main():
    load_data()
    # HTree.start_tree()
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

    # Something funky going on here
    print(allSplits(labels))

    #print(allSplits(['a', 'b', 'c', 'd']))

    # --------------------------------------

    # TODO Change input! range(0, 10) just for testing purposes
    # impurity(data.iloc[range(0, 10)])

    # TODO STYLE, uniform naming style for functions. No conform atm


main()

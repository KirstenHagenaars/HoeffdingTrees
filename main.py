import pandas as pd
import math
import numpy as np
import HTree

data = None
classes = []


def load_data():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")           #panda dataframe
    print(data.head())


def gini_index(total, inClassA, inClassB):
    gini = 1 - ((inClassA/total)^2 + (inClassB/total)^2)
    if 0 < gini < 1:
        return gini
    else:
        print("Gini index problem")


def impurity(instances):
    global classes
    inClassA, inClassB = 0, 0

    # Find number of instances of each class
    for i in instances:
        if i["class"] == classes[0]:
            inClassA = inClassA + 1
        elif i["class"] == classes[1]:
            inClassB = inClassB + 1
        else:
            print("Unexpected class in function impurity()")

    # Compute gini index
    gini_index(len(instances), inClassA, inClassB)

    # Test all possible splits
        #CODE...
    # Weight branch impurity by empirical branch probability for every possible split
        #CODE...


def main():
    load_data()
    #HTree.start_tree()
    global data
    class_labels = data["class"]
    global classes
    for c in class_labels:
        if len(classes) == 1 and classes[0] != c:
            classes.append(c[1])
            break
        else:
            classes.append(c[1])
    classA = classes[0]
    classB = classes[1]



main()

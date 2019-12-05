import pandas as pd
import math
import numpy as np
import HTree

data = None

def load_data():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")           #panda dataframe
    print(data.head())

def GINI_index():
    return abs()

def main():
    load_data()
    #HTree.start_tree()
    global data
    class_labels = data["class"]
    classes = []
    for c in class_labels:
        if len(classes) == 1 and classes[0] != c:
            classes.append(c[1])
            break
        else:
            classes.append(c[1])
    classA = classes[0]
    classB = classes[1]



main()
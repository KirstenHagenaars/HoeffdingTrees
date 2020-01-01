import pandas as pd
import HTree
import Util

data = None
classes = []


def loadData():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")  # panda dataframe


def findBestGinis(node, currentGini, labels, data, columns):  # labels off 'class', found in the main
    best, second_best = [1, None], [1, None]  # first element is the gini, second element is the corresponding attribute to split on
    for attribute in columns:
        #print(attribute)
        labels = Util.determineLabels(data[attribute])
        counted = node.countInstancesForSplit(labels, classes, attribute)
        #print(counted)
        gini = 0
        for l in range(0, len(labels)):
            gini += Util.giniIndex(counted[0][l] + counted[1][l], counted[0][l], counted[1][l])
        best, second_best = Util.updateBestGini(best, second_best, [gini / len(labels), attribute])
    best, second_best = Util.updateBestGini(best, second_best, [currentGini, None])
    #print(best)
    return best, second_best


def main(delta):
    loadData()
    global data

    # TEST CODE -------------------------
    data = data.iloc[range(0, 20)]  # TODO Change input! range(0, 10) just for testing purposes
    class_labels = data["class"]
    global classes
    classes = Util.determineLabels(class_labels)
    # --------------------------------------

    # I start following the pseudocode from here:
    columns = data.columns.tolist()
    columns.pop()
    print(Util.initialCounter(data, classes, columns))
    HT = HTree.Tree(Util.initialCounter(data, classes, columns))
    for i in range(0, int(data.size / len(data.columns))):
        instance = data.iloc[i]
        currentNode = HT.findLeaf(instance, classes, columns)
        currentNode.updateCounter(instance, columns)
        currentNode.setLabel(data, classes, columns[0])
        # Find number of instances of each class
        counted = currentNode.countInstances(data, classes, columns[0])
        total = counted[0] + counted[1]
        currentGini = Util.giniIndex(total, counted[0], counted[1])  # line 3 psuedocode TODO test gini
        print(currentGini)
        if currentGini != 0.0:  # line 15 of psuedocode, gini = 0 if all instances are of the same class
            best, second_best = findBestGinis(currentNode, currentGini, classes, data, columns)
            epsilon = 0  # TODO Util.epsilon(total, R, delta)
            if best[1] is not None and second_best[0] - best[0] > epsilon:
                currentNode.splitNode(best, data, classes, columns)
    return HT


def getAccuracy():
    # TODO use traintestsplit and compute accuracy
    # This is to test our classifier, useful in results section of report
    #use HT.predict(instance)
    HT = main()


HT = main(0.1)
currenNode = HT.root
# while currentNode.split_condition is not None:
#     print(currentNode.counter)
#     currentNode = currentNode.children[0]
for x in currenNode.children:
    print("child")
    print(x.counter)
print(currenNode.counter)


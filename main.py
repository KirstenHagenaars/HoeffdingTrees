import pandas as pd
import HTree
import Util
from sklearn.model_selection import train_test_split

allData = None
data = None
classes = []
allLabels = []


def loadData():
    # Loads the data out of the csv file into the allData dataframe
    global allData
    allData = pd.read_csv("BayesianNetworkGenerator_mushroom.csv")


def findBestGinis(node, currentGini, columns):
    # Finds the two best attributes to split on and their corresponding gini's
    best, second_best = [1, None], [1, None]        # [gini, attribute]
    for attribute in columns:
        labels = allLabels[attribute]
        counted = node.countInstancesForSplit(labels, classes, attribute)
        gini = 0
        for l in range(0, len(labels)):
            gini += Util.giniIndex(counted[0][l] + counted[1][l], counted[0][l], counted[1][l])
        best, second_best = Util.updateBestGini(best, second_best, [gini / len(labels), attribute])
    best, second_best = Util.updateBestGini(best, second_best, [currentGini, None])
    return best, second_best


def HoeffdingTree(columns, delta):
    # Creates a HoeffdingTree using the data in 'data', code corresponds to psuedocode in report
    HT = HTree.Tree(Util.initialCounter(data, classes, columns))
    for i in range(0, int(data.size / len(data.columns))):
        instance = data.iloc[i]
        currentNode = HT.findLeaf(instance)
        currentNode.updateCounter(instance, columns)
        currentNode.setLabel(data, classes, columns[0], allLabels)
        counted = currentNode.countInstances(data, classes, columns[0], allLabels)
        total = counted[0] + counted[1]
        currentGini = Util.giniIndex(total, counted[0], counted[1])
        print(currentGini)
        if currentGini != 0.0:
            best, second_best = findBestGinis(currentNode, currentGini, columns)
            epsilon = 0 #Util.epsilon(total, 0.1, delta) #TODO what is the R?
            if best[1] is not None and second_best[0] - best[0] > epsilon:
                currentNode.splitNode(best, data, classes, columns, allLabels)
    return HT


def main(delta):
    # Calculate the accuracy of the predictions when creating a Hoeffding Tree using the value delta
    loadData()
    global allData
    allData = allData.iloc[range(0, 1000)]
    print("Algorithm starts")
    class_labels = allData["class"]
    global classes
    classes = Util.determineLabels(class_labels)
    columns = allData.columns.tolist()
    columns.pop()

    X_train, X_test, y_train, y_test = train_test_split(allData.drop(columns=['class'], axis=1), class_labels)
    global data
    data = X_train
    data['class'] = y_train
    global allLabels
    allLabels = Util.getAllLabels(data, columns)

    HT = HoeffdingTree(columns, delta)
    count = 0
    y_test = y_test.to_numpy()
    for i in range(0, len(y_test)):
        count += HT.predict(X_test.iloc[i]) == y_test[i]
    print("The accuracy of the HoeffdingTree is " + str(count/len(y_test)))


main(0.1)

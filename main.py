import pandas as pd
import HTree
import Util

data = None
classes = []


def loadData():
    global data
    data = pd.read_csv("dataset_24_mushroom.csv")  # panda dataframe


# TODO finish function
def findBestGinis(instances, labels, currentGini):  # labels off 'class', found in the main

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
    return best, second_best
    # Weight branch impurity by empirical branch probability for every possible split
    # if (best[1] != None and best[0]-second_best[0]>epsilon(len(instances), range, delta)): #line 20 of pseudocode


def main():
    loadData()
    global data


    #classA = classes[0]
    #classB = classes[1]

    # TEST CODE -------------------------
    data = data.iloc[range(0, 20)]
    class_labels = data["class"]
    global classes
    classes = Util.determineLabels(class_labels)

    # Something funky going on here
    # print(allSplits(labels))

    # print(allSplits(['a', 'b', 'c', 'd']))

    # --------------------------------------
    # I start following the pseudocode from here:
    columns = data.columns.tolist()
    columns.pop()

    HT = HTree.Tree(Util.initialCounter(data, classes, columns))
    for i in range(0, int(data.size/len(data.columns))):
        instance = data.iloc[i]
        currentNode = HT.findLeaf(instance, classes, columns)
        currentNode.updateCounter(instance, columns)
        currentNode.setLabel(data, classes, columns[0])
        # if (currentNode.isPure()):
        # line 15 of psuedocode
        # Find number of instances of each class
        #counted = Util.countInstances(instances, "class", labels)

        # Compute current gini index
        #currentGini = Util.giniIndex(len(instances), counted[0], counted[1])  # line 3 psuedocode
        #if (currentGini != 0):  # line 15 of psuedocode, gini = 0 if all instances are of the same class
            # Test all possible splits
            #best, second_best = findBestGinis(instances, labels, currentGini)
            #epsilon = Util.epsilon()   line 19
            #TODO line 19 and up

    # TODO Change input! range(0, 10) just for testing purposes
    # impurity(data.iloc[range(0, 10)], classes)


main()

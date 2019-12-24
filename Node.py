import Util


class Node:
    def __init__(self, parent, children, split_condition, counter, label):
        self.parent = parent  # The parent node of this node, null for root node, leave this out?
        self.children = children  # Array of child nodes, null for leaf node, TODO only 2 children?
        self.split_condition = split_condition  # Condition node is split on, null for leaf nodes
        self.counter = counter  # Keeps track of amount of instances and their values that are at this node, n from the psuedocode
        self.label = label  # Majority class at this node

    def getParent(self):
        return self.parent

    def setParent(self, x):
        self.parent = x

    def getChildren(self):
        return self.children

    def splitNode(self, bestSplit):
        self.split_condition = bestSplit[1]
        giniKids = bestSplit[0]
        # TODO make child nodes line 21 - 26 use Util.initialCounter

    def sort(self, instance):
        # TODO Base which child to pick on split condition line 10
        return self.children[0]

    def updateCounter(self, instance, columns):
        for x in range(0, len(columns)):
            self.counter[instance[len(columns)][1]][columns[x]][instance[columns[x]][1]] += 1

    def setLabel(self, data, classes, column):
        countClass = self.countInstances(data, classes, column)
        if countClass[0] > countClass[1]:
            self.label = classes[0]
        else:
            self.label = classes[1]

    def countInstances(self, data, classes, column):
        countClass = [0, 0]
        for c in range(0, 2):
            labels = Util.determineLabels(data[column])
            for l in labels:
                countClass[c] += self.counter[classes[c]][column][l]
        return countClass

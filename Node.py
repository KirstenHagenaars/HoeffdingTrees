import Util


class Node:
    def __init__(self, counter, label):
        self.children = []  # Array of child nodes, null for leaf node
        self.split_condition = None  # attribute node is split on, null for leaf nodes
        self.counter = counter  # Keeps track of amount of instances and their values that are at this node, n from the psuedocode
        self.label = label  # Majority class at this node
        self.labels_split = None  # labels of split_condition

    def getChildren(self):
        return self.children

    def splitNode(self, bestSplit, data, classes, columns):
        self.split_condition = bestSplit[1]
        self.labels_split = Util.determineLabels(data[self.split_condition])
        initial_n = Util.initialCounter(data, classes, columns)
        print("split on " + self.split_condition)
        for l in range(0, len(self.labels_split)):
            self.children.append(Node(initial_n, None))
        # TODO gini of childs

    def sort(self, instance):
        for l in range(0, len(self.labels_split)):
            if instance[self.split_condition][1] == self.labels_split[l]:
                return self.children[l]
        print("something wrong")
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

    def countInstancesForSplit(self, labels, classes, column):
        countClass = []
        for c in range(0, 2):
            countColumn = []
            for l in range(0, len(labels)):
                countColumn.append(self.counter[classes[c]][column][labels[l]])
            countClass.append(countColumn)
        return countClass

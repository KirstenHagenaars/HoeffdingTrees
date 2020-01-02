import Util


class Node:
    def __init__(self, counter, label):
        self.children = []              # Array of child nodes, null for leaf node
        self.split_condition = None     # Attribute node is split on, null for leaf nodes
        self.counter = counter          # n from the psuedocode
        self.label = label              # Majority class at this node
        self.labels_split = None        # Labels of split_condition

    def splitNode(self, bestSplit, data, classes, columns):
        # Splits node on attribute in bestSplit
        self.split_condition = bestSplit[1]
        self.labels_split = Util.determineLabels(data[self.split_condition])
        initial_n = Util.initialCounter(data, classes, columns)
        count = self.countInstancesForSplit(self.labels_split, classes, self.split_condition)
        for l in range(0, len(self.labels_split)):
            if count[0][l] > count[1][l]:
                label = classes[0]
            else:
                label = classes[1]
            self.children.append(Node(initial_n, label))

    def sort(self, instance):
        # Returns child node instance should be sorted into
        for l in range(0, len(self.labels_split)):
            if instance[self.split_condition][1] == self.labels_split[l]:
                return self.children[l]
        print("something wrong")
        return self.children[0]

    def updateCounter(self, instance, columns):
        # Process instance by updating counter
        for x in range(0, len(columns)):
            self.counter[instance[len(columns)][1]][columns[x]][instance[columns[x]][1]] += 1

    def setLabel(self, data, classes, column):
        # Sets label to majority class
        countClass = self.countInstances(data, classes, column)
        if countClass[0] > countClass[1]:
            self.label = classes[0]
        else:
            self.label = classes[1]

    def countInstances(self, data, classes, column):
        # Returns array containing the amounts of instances at node from each class
        countClass = [0, 0]
        for c in range(0, 2):
            labels = Util.determineLabels(data[column])
            for l in labels:
                countClass[c] += self.counter[classes[c]][column][l]
        return countClass

    def countInstancesForSplit(self, labels, classes, column):
        # Returns array containing amount of instances of each class of each label in column
        countClass = []
        for c in range(0, 2):
            countColumn = []
            for l in range(0, len(labels)):
                countColumn.append(self.counter[classes[c]][column][labels[l]])
            countClass.append(countColumn)
        return countClass

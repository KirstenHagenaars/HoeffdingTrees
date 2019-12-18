class Node:
    def __init__(self, parent, children, split_condition, counter, label):
        self.parent = parent  # The parent node of this node, null for root node
        self.children = children  # Array of child nodes, null for leaf node
        self.split_condition = split_condition  # Condition node is split on, null for leaf nodes
        self.counter = counter  # Keeps track of amount of instances and their values that are at this node, n from the psuedocode
        self.label = label #Majority class at this node

    def getParent(self):
        return self.parent

    def setParent(self, x):
        self.parent = x

    def getChildren(self):
        return self.children

    def splitNode(self, condition):
        self.split_condition = condition
        # make child nodes

    def sort(self, instance):
        # TODO Base which child to pick on split condition
        return self.children[0]

    def setLabel(self, classes):
        countClass1 = 0
        #for c in range(0,1):
            #TODO set label to majority class
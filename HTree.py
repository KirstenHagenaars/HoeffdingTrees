import Node


class Tree:

    def __init__(self, n):
        self.root = Node.Node(n, None)  # root

    def findLeaf(self, instance, classes, columns):
        currentNode = self.root
        while currentNode.split_condition is not None:
            print("goto child")
            currentNode = currentNode.sort(instance)
        return currentNode

    def predict(self, instance, classes, columns): #returns predicted class of instance
        return self.findLeaf(instance, classes, columns).label

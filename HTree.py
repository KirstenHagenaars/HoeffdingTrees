import Node


class Tree:

    def __init__(self, n):
        self.root = Node.Node(None, None, None, n, None)  # root

    def findLeaf(self, instance, classes, columns):
        currentNode = self.root
        while currentNode.split_condition is not None:
            currentNode = currentNode.sort(instance)
        return currentNode
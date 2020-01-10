import Node


class Tree:

    def __init__(self, n):
        self.root = Node.Node(n, None)  # Root of the Hoeffding Tree

    def findLeaf(self, instance):
        # Returns leaf node instance gets sorted into
        currentNode = self.root
        while currentNode.split_condition is not None:
            currentNode = currentNode.sort(instance)
        return currentNode

    def predict(self, instance):
        # Returns predicted class of instance
        return self.findLeaf(instance).label

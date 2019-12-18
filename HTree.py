import Node


class Tree:

    def __init__(self, n):
        self.root = Node.Node(None, None, None, n, None)  # root

    def process(self, instance, classes, columns):
        # TODO psuedocode from line 10 until the end
        currentNode = self.root
        while currentNode.split_condition is not None:
            currentNode = currentNode.sort(instance)
        currentNode.setLabel(classes)
        #if (currentNode.isPure()):
            #line 15 of psuedocode
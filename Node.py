class Node:
  def __init__(self, parent, children, split_condition):
    self.parent = parent                            #The parent node of this node, null for root node
    self.children = children                        #Array of child nodes, null for leaf node
    self.split_condition = split_condition          #Condition node is split on, null for leaf nodes

  def getParent(self):
      return self.parent

  def setParent(self, x):
      self.parent = x

  def getChildren(self):
      return self.children

  def splitNode(self, condition):
      self.split_condition = condition
      #make child nodes
class Node:
  def __init__(self, parent, children, split_condition):
    self.parent = parent                            #The parent node of this node, null for root node
    self.children = children                        #Array of child nodes, null for leaf node
    self.split_condition = split_condition          #Condition node is split on, null for leaf nodes

  def get_parent(self):
      return self.parent

  def set_parent(self, x):
      self.parent = x

  def get_children(self):
      return self.children

  def split_node(self, condition):
      self.split_condition = condition
      #make child nodes
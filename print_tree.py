from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    s = ""
    layer = [self]
    while layer:
        next_layer = []
        for node in layer:
          s += node.val
          next_layer.extend(filter(lambda x: x != None, [node.left, node.right]))

        layer = next_layer
        next_layer = []
        s += "\n"

    return s

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print tree
# a
# bc
# defg

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
  def list_cousins(self, tree, val):
    layer_found = False
    layer = [tree]

    while not layer_found and layer:
        next_layer = []
        for node in layer:
            if (node.left and node.left.value == val) or (node.right and node.right.value == val):
                layer_found = True
                continue

            next_layer.extend(filter(lambda x: x != None, [node.left, node.right]))

        layer = next_layer

    # if not layer_found - raise exception?
    return [x.value for x in layer]





#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print Solution().list_cousins(root, 3)
# [4, 6]


def find_k_balanced(node, k):
  
  k_node, height = find_k_balanced_helper(node, k)
  if height == -1:
    return k_node
  else:
    return None

def find_k_balanced_helper(node, k):
  
  if node == None:
    return node, 0

  lnode, lheight = find_k_balanced_helper(node.left, k)
  if lheight == -1:
    return lnode, lheight

  rnode, rheight = find_k_balanced_helper(node.right, k)
  if rheight == -1:
    return rnode, rheight

  diff = abs(rheight - lheight)
  if diff > k:
    return node, -1

  return node, lheight+rheight+1


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n2.right = n3
n3.left = n4
n4.right = n5
n3.right = n6


k_node = find_k_balanced(n1, 3)
print(k_node.val)



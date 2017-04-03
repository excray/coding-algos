# Question:
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the
# depth of the two subtrees of every node never differs by more than 1.


class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.val = arg
		self.left = None
		self.right = None


def maxDepth(root):
	if root == None:
		return 0

	return max(maxDepth(root.left), maxDepth(root.right)) + 1


def minDepth(root):
	if root == None:
		return 0

	# if root.left and root.right:
	# 	return min(minDepth(root.left), minDepth(root.right)) + 1
	# elif root.left:
	# 	return minDepth(root.left) + 1
	# else:
	# 	return minDepth(root.right) + 1

	return min(minDepth(root.left), minDepth(root.right)) + 1


#     4
#    2   6
#  1  3 5  7

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n4.left = n2
n4.right = n6

# n2.left = n1
# n2.right = n3

n6.left = n5
n6.right = n7

print(maxDepth(n4))
print(minDepth(n4))


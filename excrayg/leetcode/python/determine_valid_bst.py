

# Question:
# Given a binary tree, determine if it is a valid Binary Search Tree (BST).

#BST
#All nodes in left of root are less than root val. 
#All nodes in right of root are greater than root val. 

#left subtree and right subtree are valid BST. 

class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.val = arg
		self.left = None
		self.right = None

ctr = 0
ctr1 = 0
ctr2 = 0

def is_subtree_less_than(root, val):
	global ctr1
	ctr1 += 1
	if root == None:
		return True

	return root.val < val and is_subtree_less_than(root.left, val) and \
			is_subtree_less_than(root.right, val)

def is_subtree_greater_than(root, val):
	global ctr2
	ctr2 += 1
	if root == None:
		return True

	return root.val > val and is_subtree_greater_than(root.left, val) and \
			is_subtree_greater_than(root.right, val)

def is_valid_bst(root):
	global ctr
	ctr += 1
	if root == None:
		return True

	return is_subtree_less_than(root.left, root.val) and \
			is_subtree_greater_than(root.right, root.val) and \
			is_valid_bst(root.left) and is_valid_bst(root.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

#     4
#    2   6
#  1  7 3  5

n4.left = n2
n4.right = n6

n2.left = n1
n2.right = n7

n6.left = n3
n6.right = n5

print(is_valid_bst(n4))
print(ctr,ctr1,ctr2)
ctr = 0 
ctr1 = 0
ctr2 = 0

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

n2.left = n1
n2.right = n3

n6.left = n5
n6.right = n7

print(is_valid_bst(n4))
print(ctr, ctr1, ctr2)
ctr = 0
ctr1 = 0
ctr2 = 0

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.right = n2
n2.right = n3
n3.right = n4
n4.right = n5
n5.right = n6
n6.right = n7

print(is_valid_bst(n1))
print(ctr, ctr1, ctr2)


		


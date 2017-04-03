class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.val = arg
		self.left = None
		self.right = None



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

m = float("-inf")
def find_max_path(node, m):
	# global m
	if not node:
		return 0
	l = find_max_path(node.left, m)
	r = find_max_path(node.right, m)
	m[0] = max(l+node.val+r, m[0])
	print(m)
	ret = node.val + max(l,r)
	if ret>0:
		return ret
	else:
		return 0

t=[m]
print(find_max_path(n4, t))
print(t[0])
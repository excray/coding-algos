

#Elements of programming interviews
#Heap structure
class Node:
	def __init__(self, val, l=None, r=None, p=None):
		self.data = val
		self.left = l
		self.right = r
		self.parent = p

def find_node(root):
	
#insert - insert on rightmost node and upheap.
def insert(root, elem):
	if root == None:
		return root
	root = find_node(root)
	node = Node(elem, None, None, root)
	root.right = node
	upheap(node)

def remove(root):
	if root == None:
		return root
	if root.left == None and root.right==None:
		t = root.data
		root = None
		return t
	retval = root.data
	temp = root
	root = find_node(root)
	temp.data = root.data
	root.parent.right = None
	downheap(temp)
	return retval

def downheap(root):
	if(root==None):
		return root
	child_val = None
	child_node = None
	if root.left == None and root.right == None:
		return root
	if(root.left == None):
		child_val = root.right.data
		child_node = root.right
	elif(root.right == None):
		child_val = root.left.data
		child_node = root.left
	else:
		if(root.left.data < root.right.data ):
			child_val = root.left.data
			child_node = root.left
		else:
			child_val = root.right.data
			child_node = root.right

	if(root.data > child_val):
		child_node.data = root.data
		root.data = child_val
		downheap(child_node)


# def swap(root, node):
# 	temp = root
# 	root.parent = node.parent
# 	root.left = node.left
# 	root.right = node.right
# 	root.data = node.data
# 	node.parent = temp.parent
# 	node.left = temp.left
# 	node.right = temp.right
# 	node.data = temp.data
# 	if node.left != None:
# 		node.left.parent

def upheap(node):
	if(node == None):
		return
	if(node.parent != None and node.parent.data > node.data):
		t = node.data
		x = node.parent.data
		node.parent.data = t
		node.data = x
		# swap(node.parent, node)
		upheap(node.parent)


def print_tree(root):
	if(root==None):
		return
	print_tree(root.left)
	print("node: %d" %root.data)
	print_tree(root.right)



def construct_heap(seq):
	root = Node(seq[0])
	for  i in range(1, len(seq)):
		insert(root, seq[i])
	print_tree(root)
	for i in range(len(seq)):
		print(remove(root))

seq = [4,9,8,17,26, 50,16,19]
construct_heap((seq[::-1]))
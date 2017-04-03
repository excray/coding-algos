
# // Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

# // Input: 
# //   10
# //   /  \ 
# //  2    13
# //      /
# //     11
    
# // Output:
# // 2 <-> 10 <-> 11 <-> 13

class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def print_list(node):
    temp = node
    while temp != None:
        print temp.val,
        print "->",
        temp = temp.right
    print "None" 
    

def convert_bst_to_dll(root):
    node = root
    stack = []
    stack.append(node)
    head = None
    prev = None
    succ = None
    firstTime = True
    
    while len(stack) != 0 or firstTime:
        
        firstTime = False
        
        #Go to its left most child. While pushing the path to it, in the stack.
        while node != None:
			stack.append(node)
			node = node.left
		
		#Pop the left most child. This is the node to vist. 
        ret_node = stack.pop()
		if head == None:
		    head = ret_node
		    head.left = None
    		prev = head
    	else:
    	    succ = ret_node
    	    prev.right = succ
    	    succ.left = prev
    	    prev = succ
		    
		node = ret_node
		#if visited node has right child, start the process again from right child node. 
		if node.right:
			node = self.node.right
		else:
		    node = None
		    
	if prev != None:
	    prev.right = None
	    
	return head
			
n1 = node(10)
n2 = node(2)
n3 = node(13)
n4 = node(11)

n1.left = n2
n1.right = n3
n3.left = n4

inorder(n1)
n = convert_bst_to_dll(n1)
print_list(n)



		
    
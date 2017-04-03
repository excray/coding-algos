# Given an array of the form:
# [a1,a2,a3,a4,b1,b2,b3,b4]

# Can we turn it into an array of the form:
# [a1,b1,a2,b2,a3,b3,a4,b4]

# In place?

# An android pin lock has 9 pins.
# With the following constraints, how many different combinations of passcodes are there?

# 1. Must connect at least 4 pins
# 2. All pins are distinct
# 3. If the line segment connecting any two consecutive dots 
# in the pattern passes through any other dots, 
# the other dots must have previously been in the patternself.

# o o o   1 2 3
# o o o   4 5 6
# o o o   7 8 9       47891 - invalid 45891 - valid 48951 - valid

# permutations(arr){
#     if (1,3,7,9 | 2,8 | 4,6) => increment num_invalid
#     total - num_invalid
# }



# #all: 9*8*7*6*(1 + 5 + 5 * 4 + 5 * 4 * 3 + 5 * 4 * 3 * 2 * 2)

# 4 pins, 5 pins and then add

# 1step invalid

# 2 steps
# # 4 * _1: 3 * (7*6*(1 + 5 + 5 * 4 + 5 * 4 * 3 + 5 * 4 * 3 * 2 * 2)) - corner pin

# # 4 * _2: (7*6*(1 + 5 + 5 * 4 + 5 * 4 * 3 + 5 * 4 * 3 * 2)) - middle
# # 5:

# 2nd step invalid

# _1: _1_2_8 (6*5*(1 + 4 + 4 * 3 + 4 * 3 * 2))
# 3rd step:
# _1: _1_2: 3 * _1_2_3(_7_9), 2 * _1_2(_4_6)
#     _1_5xx
# 4th step:
    


# 8 steps 

#     3*comb(7)+comb(7) #1step
#     4*4*comb(6) + 4*2*comb(6) #2step
    
    
    
    

# O(n2) right? that should be fine. 
# #   o
# # o o o
# # o o o

# # a1a2a3a4b1b2b3b4

# # a1a2a3b1a4b2b3b4
# # a1a2b1a3b2a4b3b4
# # a1b1a2b2a3b3a4b4

# def re_arrange(items):
#     n = len(items)/2
#     for i in range(1,n):
#         for j in range(0, i):
#             items[n-i+2*j], items[n-i+2*j+1] = items[n-i+2*j+1], items[n-i+2*j]
            
#     return items
    
# print(re_arrange([1,3,5,7,2,4,6,8]))
# print(re_arrange([1,3,5,7,9,2,4,6,8,10]))


# Given a board of NxM tiles, and with obstacles, how many ways are there to get from the top left tile to the bottom right tile?

# You will be given a char[][] where for some given ints d and f, char[d][f] = 'x' means that the tile at position (d, f) is an obstacle and cannot be passed, whereas char[d][f] = 'o' means that the tile at position (d, f) is passable.
# 'x' and 'o' are the only chars that will be used on the board. You can only move down and to the right.


# http://pastebin.com/7E0T9TTL

# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes . Return the new root.
 
# For Example:
# Given a binary Tree {1,2,3,4,5},
# 1
# / \
# 2 3
# / \
# 4 5
 
# return the root of the binary Tree [4,5,2, #, #, 3,1].
# 4
# / \
# 5 2
#   / \
# 3    1

#left sibling becomes parent. right sibling becomes left child. parent become right child

#http://www.pythontutor.com/visualize.html#togetherjs=2cOH2pQB1A

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def flip(node, parent):
    node1 = None
    if node.left == None:
        node1 = node
    else:
        node1 =  flip(node.left, node)
    if parent != None:
        node.left = parent.right
        node.right = parent
        parent.left = None
        parent.right = None
        
    return node1
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

inorder(flip(n1, None))


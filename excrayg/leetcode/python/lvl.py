
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        
        if root == None:
            return "#,"
        p = str(root.val)+","
        p+=self.serialize(root.left)
        p+=self.serialize(root.right)
        return p

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''

    def d_h(self, nodes, i):
        if i >= len(nodes):
            return None

        if nodes[i] == "#":
            return None

        root = TreeNode(int(nodes[i]))
        root.left = self.d_h(nodes, 2*i+1)
        root.right = self.d_h(nodes, 2*i+2)
        return root

    def deserialize(self, data):
        # write your code here
        data = data.strip()
        data=data[:len(data)-1]
        nodes = data.split(",")
        
        head = self.d_h(nodes, 0)
                
        return head    

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

s = Solution()
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
t=s.serialize(root)
print(t)
s.inorder(s.deserialize(t))

class Root:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
    return



def contruct_bt(inorder):
    global pre
    if len(inorder) == 0:
        return None

    if len(inorder) == 1:
        pre = pre[1:]   
        return Root(inorder[0])
    
    root = Root(pre[0])
    print(pre, inorder)
    index = inorder.index(root.val)
    pre = pre[1:]
    root.left = contruct_bt(inorder[:index])
    root.right = contruct_bt(inorder[index+1:])
    
    return root
    

# a = Root(1)
# b = Root(2)
# c = Root(3)
# d = Root(4)

# a.left = b
# a.right = c
# c.left = d
pre = [1,2,3,4]
inorder(contruct_bt([2,1,4,3]))
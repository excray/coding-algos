

def lev_dist(a, b):
    l_a = len(a)+1
    l_b = len(b)+1
    d = [[0]*l_b for t in range(l_a)]
    for i in range(l_a):
        d[i][0] = i
    for j in range(l_b):
        d[0][j] = j
    for i in range(1,l_a):
        for j in range(1,l_b):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i-1][j-1], min(d[i-1][j], d[i][j-1]))

    print(d[l_a-1][l_b-1])


#lev_dist("abc", "abc")
#lev_dist("qwe", "we")

class Node:
    def __init__(self, val):
        self.val  = val
        self.left = None
        self.right = None

def build_bst_helper(arr, l, r):
    if l <= r:
        m = l+(r-l)/2
        n = Node(arr[m])
        n.left = build_bst_helper(arr, l, m-1)
        n.right = build_bst_helper(arr, m+1, r)
        return n
    else:
        return None

def inorder(n):
    if n != None:
        inorder(n.left)
        print(n.val)
        inorder(n.right)

def build_bst(sorted_arr):
    n = build_bst_helper(sorted_arr, 0, len(sorted_arr)-1)
    inorder(n)

build_bst(list(range(10)))




#merge two BST

class Node:
    def __init__(self, val, l=None, r=None):
        self._val  = val
        self.left = l
        self.right = r

    def __repr__(self):
        return ("Node: {} ".format(self._val))

def print_list(node):
    print("Printing DLL:")
    while node:
        print("{} ".format(node._val), end="")
        node = node.right

    print()

def print_tree(node):
    print("Printing tree:")
    stack = []
    done = False
    while not done:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) != 0:
                node = stack.pop()
                print("{} ".format(node._val), end="")
                node = node.right
            else:
                done = True

    print()

def count_nodes_in_dll(head):
    node = head
    c = 0
    while node:
        node = node.right
        c+=1
    return c

def convert_dll_to_bst(head):
    n = count_nodes_in_dll(head)
    return convert_dll_to_bst_helper([head], n)

def convert_dll_to_bst_helper(node_ptr, n):
    if n <= 0:
        return None
    else:
        left = convert_dll_to_bst_helper(node_ptr, int(n/2))
        node = node_ptr[0]
        node_ptr[0] = node.right
        node.left = left
        right = convert_dll_to_bst_helper(node_ptr, n-int(n/2)-1)
        node.right = right
        return node

def convert_bst_to_dll(root):
    head = convert_bst_to_dll_helper(root)
    head.left.right = None
    head.left = None
    return head

def convert_bst_to_dll_helper(root):
    if root is None:
        return None
    else:
        left_list = convert_bst_to_dll_helper(root.left)
        right_list = convert_bst_to_dll_helper(root.right)
        
        left_tail = None
        if left_list:
            left_tail = left_list.left
            left_tail.right = root
            root.left = left_tail
            left_tail = root
        else:
            left_list = root
            left_tail = root

        right_tail= None
        if right_list:
            right_tail = right_list.left
            left_tail.right = right_list
            right_list.left = left_tail
        else:
            right_tail = left_tail

        right_tail.right = left_list
        left_list.left = right_tail

        return left_list

def merge_circular_dll(left_dll, right_dll):
    if left_dll is None:
        return right_dll
    elif right_dll is None:
        return left_dll
    else:
        # print_list(left_dll)
        # print_list(right_dll)
        left_dll_head = left_dll
        left_dll_tail = left_dll_head.left
        right_dll_head = right_dll
        right_dll_tail = right_dll_head.left
        left_dll_tail.right = right_dll_head
        right_dll_head.left = left_dll_tail
        right_dll_tail.right = left_dll_head
        left_dll_head.left = right_dll_tail
        return left_dll_head

def merge_sorted_dll(left_dll, right_dll):
    if left_dll is None:
        return right_dll
    elif right_dll is None:
        return left_dll
    else:
        result = Node(-1)
        dummyNode = result

        while left_dll and right_dll:
            if left_dll._val < right_dll._val:
                result.right = left_dll
                left_dll.left = result
                result = left_dll
                left_dll = left_dll.right
            else:
                result.right = right_dll
                right_dll.left = result
                result = right_dll
                right_dll = right_dll.right

        if left_dll:
            result.right = left_dll
        else:
            result.right = right_dll

        return dummyNode.right

def merge_two_bst(root1, root2):
    node1 = convert_bst_to_dll(root1)
    print_list(node1)
    node2 = convert_bst_to_dll(root2)
    print_list(node2)
    node = merge_sorted_dll(node1, node2)
    print_list(node)
    root = convert_dll_to_bst(node)
    return root


def create_bst(l):
    if len(l) == 0:
      return None
    else:
        n = len(l)
        m = int(n/2)
        node = Node(l[m])
        node.left = create_bst(l[:m])
        node.right = create_bst(l[m+1:])
        return node

def main():
    root1 = create_bst([2,5,11,17,23])
    root2 = create_bst([3,7,13,19])
    root = merge_two_bst(root1, root2)
    print_tree(root)


main()

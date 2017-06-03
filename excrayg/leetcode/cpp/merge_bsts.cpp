// Given two BST, Merge them.
// Convert BST to DLL. 
// Merge two DLL. 
// Convert DLL to BST.

// How to convert BST to DLL. 

/*
1) Do inorder traversal of BST and create a DLL. 
2) Have an inorder iterator, 
   it->next(). node.left = prev, prev.right = node
*/

#include <iostream>
#include <stack>

using namespace std;

struct Node
{
    Node(int val)
    {
        this->val = val;
    }
    int val; 
    Node* left;
    Node* right;
};

class BSTIterator
{
    public:
        BSTIterator(Node* root)
        {
            Node* temp = root;
            while(temp)
            {
                bst_stack.push(temp);
                temp = temp->left;
            }
        }
        
        bool hasNext()
        {
            return !bst_stack.empty();
        }
        
        Node* next()
        {
            Node* top = bst_stack.top();
            bst_stack.pop();
            
            if(top->right)
            {
                Node* temp = top->right;
                while(temp)
                {
                    bst_stack.push(temp);
                    temp = temp->left;
                }
            }
            return top;
        }
    private:
        stack<Node*> bst_stack;
};

Node* convert_bst_to_dll(Node* root)
{
    BSTIterator bIter(root);
    Node *prev = NULL, *head = NULL;
    
    while(bIter.hasNext())
    {
        Node* curr = bIter.next();
        if(!head)
        {
            head = curr;
        }
        curr->left = prev;
        if(prev)
        {
            prev->right = curr;
        }
        prev = curr;
    }
    
    return head;
}

Node* merge_two_dll(Node* first, Node* second)
{
    Node* dummy =  new Node(0);
    Node* head = dummy;
    while(first && second)
    {
        Node* curr = NULL;
        if(first->val < second -> val)
        {
            curr = first;
            first = first->right;
        }
        else
        {
            curr = second;
            second = second->right;
        }
        dummy->right = curr;
        curr->left = dummy;
        dummy = curr;
        curr = curr->right;
    }
    
    if(first)
    {
        dummy->right = first;
    }
    else
    {
        dummy->right = second;    
    }
    
    return head->right;
}

int count_nodes_in_dll(Node* head);
Node* convert_dll_to_bst_helper(Node** head, int n);

Node* convert_dll_to_bst(Node* head)
{
    // Count the nodes in the DLL. 
    int n = count_nodes_in_dll(head);
    return convert_dll_to_bst_helper(&head, n);
}

int count_nodes_in_dll(Node* head)
{
    int count = 0;
    while(head)
    {
        count += 1;
        head = head->right;
    }
    
    return count;
}

Node* convert_dll_to_bst_helper(Node** head, int n)
{
    if(n == 0)
    {
        return NULL;
    }
    else
    {
        Node* left = convert_dll_to_bst_helper(head, n/2); 
        Node* root = *head;
        root->left = left;
        *head = (*head)->right;
        Node* right = convert_dll_to_bst_helper(head, n-n/2-1);
        root->right = right;
        return root;
    }
}

void printNodes(Node* root)
{
    while(root)
    {
        cout << root->val << " ";
        root = root->right;
    }
    cout << endl;
}

void printTree(Node* root)
{
    if(root)
    {
        printTree(root->left);
        cout << root->val << " ";
        printTree(root->right);
    }
}

Node* merge_bst(Node* bst1, Node* bst2)
{
    Node* dll1 = convert_bst_to_dll(bst1);
    Node* dll2 = convert_bst_to_dll(bst2);
    
    printNodes(dll1); printNodes(dll2);
    Node* merged = merge_two_dll(dll1, dll2);
    printNodes(merged);
    
    return convert_dll_to_bst(merged);
}

int main()
{
    Node* n1 = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(4);
    Node* n5 = new Node(5);
    Node* n6 = new Node(6);
    
    n2->left = n1;
    n2->right = n3;
    
    n5->left = n4;
    n5->right = n6;
    
    Node* merged = merge_bst(n2, n5);
    printTree(merged);
    
    return 0;
}
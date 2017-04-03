# Definition for singly-linked list with a random pointer.

# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    
    def reverseList(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
            
        # dummy = ListNode(-1, head)
        #1-2-3-None
        #     2 - 1 - None
        prev = None
        while head:
            n = head.next
            head.next = prev
            prev = head
            head = n
            
        return prev
        
    def merge(self, head, mid):
        a = head
        b = mid
        
        while a and b:
            t1 = a
            t2 = b
            a.next = b
            b.next = t1.next
            
            a = t1.next
            b = t2.next
        
        return head
    
    def reorderList(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
            
        n = 0
        t = head
        while t:
            t = t.next
            n+=1
        
        m = int(n/2)
        t = head
        prev_t = None
        i = 0
        while i < m:
            prev_t = t
            t = t.next
            i+=1
        prev_t.next = None
        midList = self.reverseList(t)
        return self.merge(head, midList)

n1 = ListNode(1)
n2 = ListNode(1, n1)

head = n2
s = Solution()
h = s.reorderList(head)


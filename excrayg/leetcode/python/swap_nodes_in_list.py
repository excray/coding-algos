# 22. Swap Nodes in Pairs
# Code it now: https://oj.leetcode.com/problems/swap-nodes-in-pairs/ Difficulty: Medium, Frequency: Medium
# Question:
# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
# Given 1  2  3  4, you should return the list as 2  1  4  3.
# Your algorithm should use only constant space. You may not modify the values in the
# list, only nodes itself can be changed.
# Example Questions Candidate Might Ask:
# Q: What if the number of nodes in the linked list has only odd number of nodes?
# A: The last node should not be swapped.

# a and b point to first and second node. 

# 1.next = a, a.next = b. b.next = 2
# 1.next = b, b.next = a, a.next = 2

class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.val = arg
		

def swap_nodes(a):
	if not a or not a.next
		return a

	dummy = Node(-1)
	a1 = a
	b1 = a.next
	prev = dummy
	prev.next = a1
	last = b1.next

	while a1 and b1:
		prev.next = b1
		b1.next = a1
		a1.next = last
		prev = last
		if last:
			a1 = last.next
			if a1:
				b1 = a1.next
				if b1:
					last = b1.next

	return dummy.next


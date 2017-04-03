#!/usr/local/bin/python
import sys

def cyclic_search(arr, elem):
	if len(arr) == 0:
		return -1
	if len(arr) == 1:
		return 0
	mid = int(len(arr)/2)
	if mid-1 < 0:
		pass
	if arr[mid-1] > arr[mid] and arr[mid] < arr[mid+1]:
		return mid
	if arr[0] < arr[mid]:
		if arr[:-1] < arr[0]:
			return cyclic_search(arr[mid+1:])


def sqrt(elem):
	if elem == 0 or elem == 1:
		return elem

	left = 0
	right = elem
	while(left + 1 < right):
		mid = left + int((right-left)/2)
		print(left,mid,right)
		sqr = mid*mid
		if sqr == elem:
			return mid
		elif sqr < elem:
			left = mid 
		else:
			right = mid - 1

	if right * right <= elem:
		return right
	return left

# print(sqrt(10))
# print(sqrt(401))
# print(sqrt(2))
# print(sqrt(16))

#Strings algos
#convert strings to int and int to strings 
def atoi(s):
	if len(s) == 0:
		assert("Null string passed")

	sign = 1
	startIndex = 0
	if s[0] == "+":
		startIndex = 1
	if s[0] == "-":
		sign = -1
		startIndex = 1

	res = 0
	dig = 1
	for c in s[startIndex:]:
		res *= dig
		ascii_c = ord(c) - ord('0')
		# print(ascii_c)
		if ascii_c >= 0 and ascii_c <= 9:
			res += ascii_c
			dig = 10
		else:
			return ("Error in encoding")
			# return ""


	return res*sign



# print(atoi("123"))
# print(atoi("1"))
# print(atoi("12a"))
# print(atoi("-11"))

class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.data = arg
		self.left = None
		self.right = None


n = Node(5)
		











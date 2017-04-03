
def bin_search(arr, s, e, x):
	if s < e:
		m = s + int((e-s)/2)
		if arr[m] == x:
			return m

		if x < arr[m]:
			return bin_search(arr, s, m, x)
		else:
			return bin_search(arr, m+1 , e, x )

	return -1

#[1,2,3] tgt = 5
def two_sum_sort(arr, tgt):
	print("Running two_sum_sort")
	for idx, elem in enumerate(arr):
		elem_to_find = tgt - elem
		l = bin_search(arr, 0, idx, elem_to_find)
		if l != -1:
			print("Found the two elems at {} and {}".format(idx, l))
			
		r = bin_search(arr, idx, len(arr), elem_to_find)
		if r != -1:
			print("Found the two elems at {} and {}".format(idx, r))
			


two_sum_sort([1,2,3,4], 5)
two_sum_sort([1,2,3,4,5], 9)
two_sum_sort([1,2], 3)
two_sum_sort([1,2,3,4], 15)

def two_sum_sort_two_ptr(arr, p1, p2, tgt):
	if p1 > p2:
		print("Not found")
		return

	if arr[p1] + arr[p2] == tgt:
		print("Found the two elems at {} and {}".format(p1, p2))

	if arr[p1] + arr[p2] > tgt:
		return two_sum_sort_two_ptr(arr, p1, p2-1, tgt)
	else:
		return two_sum_sort_two_ptr(arr, p1+1, p2, tgt)

	return

print("Running")
two_sum_sort_two_ptr([1,2,3,4], 0, 3, 5)
print("Running")
two_sum_sort_two_ptr([1,2,3,4,5], 0, 4, 9)
print("Running")
two_sum_sort_two_ptr([1,2], 0, 1, 3)
print("Running")
two_sum_sort_two_ptr([1,2,3,4], 0, 3, 15)

def lower(c):
	if ord(c) >= ord('A') and ord(c) <= ord('Z'):
		return chr(ord('a')+(ord(c)-ord('A')))

	return c

def is_valid_palindrome(arr, p1, p2):
	# print(p1,p2)
	if p1 >= p2:
		return True

	left_chr = arr[p1]
	right_chr = arr[p2]

	if not (ord(lower(left_chr)) >= ord('a') and ord(lower(left_chr)) <= ord('z')):
		p1+=1
		return is_valid_palindrome(arr, p1, p2)

	elif not (ord(lower(right_chr)) >= ord('a') and ord(lower(right_chr)) <= ord('z')):
		p2-=1
		return is_valid_palindrome(arr, p1, p2)

	elif lower(left_chr) == lower(right_chr):
		return is_valid_palindrome(arr, p1+1, p2-1)
	else:
		return False

s = "A man, a plan, a canal: Panama."
print(is_valid_palindrome(s, 0, len(s)-1))












		

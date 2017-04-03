

def find_max_subarray(a):
	#edge case, if all numbers are negative. 
	curr_sum = 0 
	max_sum = a[0]

	for i in a:
		curr_sum += i
		if curr_sum < 0:
			curr_sum = 0
		max_sum = max(max_sum, curr_sum)

	return max_sum

def find_max_subarray1(a):
	max_ending_here = a[0]
	max_so_far = a[0]

	for i in range(1, len(a)):
		print(max_so_far, max_ending_here)
		max_ending_here = max(max_ending_here+a[i], a[i])
		# max_ending_here += a[i]
		max_so_far = max(max_so_far, max_ending_here)

	return max_so_far

a = [-2, -1, -3, -4, -1, 2, 1, -5, 4]
print(find_max_subarray(a))
print(find_max_subarray1(a))


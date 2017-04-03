

# [1,5,7,9,10]

# [7,9,10,1,5]

def bin_search(arr, start, end, val):
	if start >= end:
		return False

	mid = start + int((end-start)/2)
	if arr[mid] == val:
		return True

	if val < arr[mid]:
		return bin_search(arr, start, mid-1, val)
	else:
		return bin_search(arr, mid+1, end, val)


def mod_bin_search(arr, start, end, val):
	
	if start >= end:
		return False

	mid = start + int((end-start)/2)
	if arr[mid] == val:
		return True

	if arr[start] <= arr[mid]:
		if val > arr[mid]:
			return mod_bin_search(arr, mid+1, end, val)
		else:
			if arr[start] <= val:
				return bin_search(arr, start, mid-1, val)
			else:
				return mod_bin_search(arr, mid+1, end, val)
	else:
		if val > arr[mid]:
			return bin_search(arr, mid+1, end, val)
		else:
			return mod_bin_search(arr, start, mid-1, val)

v=[7,9,10,1,5]
for i in v:
	print(mod_bin_search(v, 0, len(v), 5))
print(mod_bin_search(v, 0, len(v), 0))
print(mod_bin_search(v, 0, len(v), 15))




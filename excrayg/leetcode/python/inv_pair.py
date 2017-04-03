def count_inv_pairs( arr ):
	count_inv_pairs_helper(arr, 0, len(arr)-1)

def count_inv_pairs_helper(arr, start, end):
	mid = start + (end-start)/2

	if ( start > end ):
		return 0

	count = count_inv_pairs_helper(arr, start, mid)
	count += count_inv_pairs_helper(arr, mid+1, end)
	count += merge_count(arr, start, mid, end)

	return count

def merge_count(arr, start, mid, end):
	i = start, j = mid+1, count = 0, temp = []
	while i <= mid && j <= end:
		if arr[i] > arr[j]:
			count += mid - i
			i++
			temp.append(arr[j])
		else:
		    	j++
			temp.append(arr[i])

	while i <= mid:
		temp.append(arr[i])
		i++
	while j <= end:
		temp.append(arr[j])
		j++
	for( i = start i < end i++)
		arr[i] = temp.popFront()
	
return count

print(count_inv_pairs(4,3,2,1))


def find_max_arr(input_arr):
  
  start_idx = 0
  max_len = float("-inf")

  h = {}

  for idx, elem in enumerate(input_arr):
    if elem in h:
      last_occur_idx = h[elem]
      if last_occur_idx >= start_idx:
        start_idx  = last_occur_idx + 1
        h[elem] = idx
    else:
      h[elem] = idx
    max_len = max(max_len, idx - start_idx + 1)
      
  return max_len

arr = [5,7,5,9,11,2,11,10,9]
print(find_max_arr(arr))
arr = [1,2,3,4,4,5,6,7,8]
print(find_max_arr(arr))
arr = [1,1,1]
print(find_max_arr(arr))
arr = [1,2,3,4,1,6,7,4,5,5]
print(find_max_arr(arr))

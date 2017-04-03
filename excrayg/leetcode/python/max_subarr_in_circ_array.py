# problem1: rebuild a bt from its preorder and inorder traverse

# problem2: find closest sub array sum. 
# given an array and a target number, return the sum of sub array that closest to the target

# [-4, 3, -2, 1, 2]  target=0 o(n^2)

# [ 0 , 4 ,  1 , 3 , 2]

# two pointers, one at start, one at end and try shrinking it.. I need to think

# [-4, 3, -2, 1, 2]
# sum[i] = sum[0~i]
# sum: [-4, -1, -3, -2, 0]
# sum[j] - sum[i] closest to target
# t[i] = sum[i] + target
# t[i] closest to sum[j] s.t. i < j
# rank_sort sum => rank
# search t[i] in rank, o(logn)
# o(nlogn)


# [1,2,25,2,2] tgt = 27

# lsum = [1,3,28,30,32]
# t = [28, 30, 55, 57, 59]

# rank_sort(lsum) => rank[i]:the rank of lsum[i] = [0,1,2,3,4]
# for each i in t : 
#     t[0] lsum[rank[mid]] rank[2] lsum[2] = 28 = t[0] => return target immediately
#     rank[
# find the index of lsum of 28, 2, 0~2 0+1 2

# index at which t[i] is found in lsum is end index 
# and i+1 is start index

# you find the indices of rank_sort by noting the indexes that get swapped while sorting lsum. 
# if you run rank_sort indexes on original array, you should get the sorted array
# quick_sort, 
# rank[i] = i
# swap(lsum[a], lsum[b]); swap(rank[a], rank[b]);# 


# find closest sum of subset of an array to a target
# 
# [-1, 4, 9] target = 8, return 8 = -1 + 9

# a counting rank sort
# def rank_sort(nums):
#     n = len(nums)
#     m = 100
#     rank = [0 for i in range(0, n)]
#     bucket = [0 for i in range(0, m)]
#     for i in range(0, n):
#         ++bucket[nums[i]]
#     for i in range(1, m):
#         bucket[i] += bucket[i - 1]
#     for i in range(n-1, -1, -1):
#         rank[--bucket[nums[i]] = i
#     return rank
#     n!

# [1,1,1,0,0,1,1]

# [3,6,2,3,5,1]

# player 1
# [1,0,0,1,1,1]

# player 2
# [1]          [1,1]  - player 1
#  /        /            
# [1,0,0,0.., 1], [1,1,1]      - player 2 
# /
# [1,1,0..., 1,1]
# # -*- coding: ascii -*-


# compute the maximum subarray sum in circular array
# Given a circular array A, compute it maximum subarray sum in O(n) time. Can you devise it in
# O(1) space too. 
# [1, -1, 1] 2


def find_max_sum(A):
    if len(A) == 1:
        if A[0] < 0:
            return 0
        
    max_sum = float("-inf")   
    curr_sum = 0
    print(A)
    for i, a in enumerate(A):
        curr_sum += a
        if a < 0:
            curr_sum = find_max_sum(A[:i]) + find_max_sum(A[i+1:])
            max_sum = max(curr_sum, max_sum)
            break
        else:
            max_sum = max(curr_sum, max_sum)
            
    return max_sum
    
print(find_max_sum([4, -1, 4, -5, 1]))

def find_max_sum1(A, s, e, cache):
    if e-s == 1:
       if A[s] < 0:
           cache[s][e] = 0
           return 0
           
    if s in cache and e in cache[s]:
        return cache[s][e]
           
    max_sum = float("-inf")
    curr_sum = 0
    t = s 
    r = e
    while s < e:
        curr_sum += A[s]
        if curr_sum < 0:
            curr_sum = find_max_sum1(A, t, s, cache) + find_max_sum1(A, s+1, e, cache)
            max_sum = max(max_sum, curr_sum)
            break
        else:
            max_sum = max(curr_sum, max_sum)
            
        s+=1
        
    cache[t][r] = max_sum
    return max_sum
    
    
def run_max():
    A = [4, -1, 4, -5, 1]
    n = len(A)
    cache = [ [0]*(n+1) for i in range(n+1)]
    print(find_max_sum1(A, 0, n, cache))
    
run_max()
            

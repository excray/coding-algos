# 35. Spiral Matrix
# Code it now: https://oj.leetcode.com/problems/spiral-matrix/ Difficulty: Medium, Frequency: Medium
# Question:
# Given a matrix of m ✕ n elements (m rows, n columns), return all elements of the
# matrix in spiral order.
# For example, given the following matrix:
# [
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

#have a function to print outer layer of matrix


def print_spiral(mat):
	m = len(mat)
	n = len(mat[0])
	i = 0
	j = 0
	l = []
	while m > 1 and n > 1:
		print_outer_layer(mat, i, j, m, n, l)
		i+=1
		j+=1
		m-=2
		n-=2

	if m == 1:
		#print ith row
		for a in range(j, n):
			l.append(mat[i][a])
	elif n == 1:
		#print jth column
		for a in range(i, m):
			l.append(mat[a][j])

	return l


def print_outer_layer(mat, i, j, m, n, l):
	#print i'th row
	for a in range(j, n):
		l.append(mat[i][a])

	#print nth column
	for a in range(i+1, m):
		l.append(mat[a][n-1])

	#print mth row in reverse
	for a in range(n-2, j-1, -1):
		l.append(mat[i][a])

	#print jth column in reverse.
	for a in range(m-2, i-1, -1):
		l.append(mat[a][j])


mat = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
print(print_spiral(mat))



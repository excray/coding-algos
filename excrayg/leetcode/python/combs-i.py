

def helper(result, s, cur, i):
	for j in range(i, len(s)):
		if j > i and s[j-1] == s[j]:
			continue
		cur.append(s[j])
		result.append(list(cur))
		helper(result, s, cur, j+1)
		cur.pop()

def comb(s):
	s_s = []
	s_s.append([])
	if s == [] or s == None:
		return s_s
	s.sort()
	helper(s_s, s, [], 0)
	print(s_s)

s = [1,2,2]
comb(s)




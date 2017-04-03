

def max_prod(a):
	print(a)
	mx1 = a[0]
	mn1 = a[0]
	maxAns = a[0]
	for i in range(1, len(a)):
		t = a[i]
		mx = mx1
		mn = mn1 
		mx1 = max(max(mx*t, t), mn*t)
		mn1 = min(min(mx*t, t), mn*t)
		maxAns = max(mx1, maxAns)
		print(mx1, mn1, maxAns)
	return maxAns

a=[2,3,-2,-4]
print(max_prod(a))

a=[2,3,-2,4]
print(max_prod(a))
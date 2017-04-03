

def ins(A):
    i = 0
    n = len(A)
    while i < n:
        cand = A[i]
        j = i-1

        while j >= 0:
            if cand > A[j]:
                break
            A[j+1] = A[j]
            j-=1
        A[j+1] = cand
        i+=1
    print(A)
ins([5,4,3,2])
ins([1,4,2,1])


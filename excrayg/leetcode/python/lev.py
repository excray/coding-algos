
def h(A, a, B, b, d, solns):

    if (a,b) in d:
        return d[(a,b)]

    if a == len(A):
        d[(a,b)] = len(B) - b
        solns[(a,b)] = 'i'
        return d[(a,b)]

    if b == len(B):
        d[(a,b)] = len(A) - a
        solns[(a,b)] = 'd'
        return d[(a,b)]


    if A[a] == B[b]:
        d[(a,b)] = h(A, a+1, B, b+1, d, solns)
        solns[(a,b)] = 's'
        return d[(a,b)]
    else:
        i = h(A, a, B, b+1, d, solns) + 1
        de = h(A, a+1, B, b, d, solns) + 1
        r = h(A, a+1, B, b+1, d, solns) + 1

        if i <= de and i <= r:
            solns[(a,b)] = 'i'
            d[(a,b)] = i

        if de <= i and de <= r:
            solns[(a,b)] = 'd'
            d[(a,b)] = de

        if r <= i and r <= de:
            solns[(a,b)] = 'r'
            d[(a,b)] = r

        return d[(a,b)]

def edit_distance(A, B):
    solns = {}
    di = {}
    d = h(A, 0, B, 0, di, solns)
    # print(di)
    print("Min distance: {}".format(d))
    # print(solns)
    a = 0
    b = 0
    while a < len(A) and b < len(B):
        soln = solns[(a,b)]
        if soln == 's':
            print("Step A: {} and B: {}".format(a,b))
            a+=1
            b+=1
            continue
        if soln == 'r':
            print("replace A: {} and B: {} with value: {}".format(a,b, B[b]))
            a+=1
            b+=1
            continue
        if soln == 'i':
            print("Insert A: {} and B: {} with value: {}".format(a,b, B[b]))
            b+=1
            continue
        if soln == 'd':
            print("Delete A: {} and B: {} with value: {}".format(a,b, A[a]))
            a+=1
            continue

    if a == len(A):
        print("Insert {} chars from B".format(len(B)-b))

    if b == len(B):
        print("Delete {} chars from A".format(len(A)-a))

# edit_distance('anshuman', 'antihuman')
edit_distance('abcd', 'abc')



def min_coins(S, index, V, count):
    if S < 0:
        return float("inf")
    
    if S == 0:
        return count

    if index >= len(V):
        return float("inf")

    i = index
    count = min( min_coins(S, i+1, V, count), min_coins(S-V[i], i, V, count+1))

    return count


S = 7
v=[1,2,3, 7]
count = float("inf")

print(min_coins(S, 0, v, 0))



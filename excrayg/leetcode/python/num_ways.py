
def count1(k, score_ways):
    combinations = [0]*(k+1)
    combinations[0] = 1
    for score in score_ways:
        for j in range(score, k+1):
            combinations[j] += combinations[j-score]
    return combinations[k]

def count2(k, score_ways, i, d):
    if k == 0:
        return 1
    n = len(score_ways)
    if i == n:
        return 0

    if k < 0:
        return 0


    if (i,k) in d:
        return d[(i,k)]

    d[(i,k)] = count2(k-score_ways[i], score_ways, i, d) + \
                    count2(k, score_ways, i+1, d)

    return d[(i,k)]


k = 120
score_ways = [2,3,4,5,7]

print(count1(k, score_ways))
print(count2(k,score_ways,0,{}))




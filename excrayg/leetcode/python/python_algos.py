

def coin_min(coins, S):
    t = [float("inf")]*(S+1)
    t[0] = 0
    for i in range(1,S+1):
        if i in coins:
            t[i] = 1
            continue
        for j in range(i-1, 0, -1):
            if t[i-j]+t[j] < t[i]:
                t[i] = t[i-j]+t[j]

    return t[S]

def coin_min1(coins, S):
    t = [float("inf")]*(S+1)
    coins_list = [None]*(S+1)
    print(coins_list)   
    t[0] = 0
    coins_list[0] = []
    for i in range(1,S+1):        
        for j in range(0, len(coins)):
            if coins[j]<=i and t[i-coins[j]]+1 < t[i]:
                t[i] = t[i-coins[j]]+1
                coins_list[i] = coins_list[i-coins[j]]+[coins[j]]

    return t[S], coins_list[S]
# def dfs(G, node, discover_time, finish_time, Seen=None, time=0):
#     if Seen is None: Seen = set()
#         discover_time[node] = time; time+=1
#         Seen.add(node)
#         for u in G[node]:
#             if u in Seen: continue
#                 time = dfs(G, u, discover_time, finish_time, Seen, time)
#         finish_time[node] = time; time += 1
#         return time

# def dfs_1(G, node, Seen):
#     C = set()
#         C.add(node)
#         Seen.add(node)
#         for u in G[node]:
#             if u in Seen: continue
#                 C=C|dfs_1(G, u, Seen)
#         return C

# G = {'a':['c', 'b'], 'b':['d', 'i', 'e'], 'c': ['d'], 'd':['a', 'h'], 'e':['f'], 'f':['g'], 'g':['e', 'h'], 'h':['i'], 'i':['h']}
# discover_time = dict()
# finish_time = dict()
# dfs(G, 'a', discover_time, finish_time)
# #print(discover_time)
# #print(finish_time)

# def dfs_topsort(G):
#     Seen, res = set(), []
#         def recurse(node):
#             if node in Seen: return
#                 Seen.add(node)
#                 for neigh in G[node]:
#                     #if neigh in Seen: continue
#                         recurse(neigh)
#                 res.append(node)
#         for u in G:
#             recurse(u)
#         res.reverse()
#         return res

# res = dfs_topsort(G)
# #print(res)

# def iddfs(G, node):
#     yielded = set()
#         def recurse(G, node, depth, Seen=None):
#             if node not in yielded:
#                 #yield node
#                         yielded.add(node)
#                 if depth == 0: return
#                 if Seen is None: Seen = set()
#                 Seen.add(node)
#                 for neigh in G[node]:
#                     if neigh in Seen: continue
#                         recurse(G, neigh, depth-1, Seen)
#                 #print(depth, Seen)
#         n = len(G)
#         for d in range(n):
#             if len(yielded) == n: break
#                 recurse(G, node, d)
#         #print(yielded)
# # for n in iddfs(G, 'a'):
# #       #print(n)
# iddfs(G, 'a')


# def transpose(G):
#     GT = {}
#         for u in G:
#             GT[u] = set()
#         for u in G:
#             for v in G[u]:
#                 GT[v].add(u)
#         return GT

# def SCC(G):
#     GT = transpose(G)
#         sccs, seen = [], set()
#         for u in dfs_topsort(G):
#             print(u)
#                 if u in seen: continue
#                 # print(u)
#                 C = dfs_1(GT, u, seen)
#                 #seen.update(C)
#                 sccs.append(C)
#         return sccs

# print(SCC(G))
# GT = transpose(G)
# print(dfs_topsort(GT))
coins = [1,3,5]
S = 11
print(coin_min1(coins, S))

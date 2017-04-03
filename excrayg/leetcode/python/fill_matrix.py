# given a matrix, 0 represents for white place, other represents for colored place, 
# and given a point and a new color, fill the point and the white places surrounding the point of the new color. do it iteratively.



#Do a bfs search.

from collections import deque

m = [[1,0,2], [2,0,5], [1,1,1]]

n = len(m[0])
q = deque()
v = set()
c = 5

x = 1
y = 1

# //from a point, i check its adjacent neighbours, if any of them is 0, 
# //i add them to queue. then do a bfs. 
# // i also keep track of visited nodes?
# // no need for visited
# // because i change 0 to some color, that is like visited.

q.append((x,y))

while len(q) != 0:
    n = q.popleft()
    print(n, "l")
    x = n[0]
    y = n[1]
    
    m[x][y] = c
    
    if x > 0:
        if (x-1,y) not in v and m[x-1][y] == 0:
            q.append((x-1, y))
    
    if x < n:
        if (x+1,y) not in v and m[x+1][y] == 0:
            q.append((x+1, y))
            
    if y > 0:
        if (x,y-1) not in v and m[x][y-1] == 0:
            q.append((x, y-1))
    
    if y < n:
        if (x,y+1) not in v and m[x][y+1] == 0:
            q.append((x, y+1))
            
    v.add((x,y))
    
print(m)

//iterative dfs

// if tree is like this

root level 1

1000 nodes in  level 2, each node in level 2 connects to all nodes in level 3

1000 nodes in level 3

this is BFS
in level 2, when you are visiting one node, you push 1000 nodes in queue
when you visit next node, you push 1000 more nodes, so now queue has 2000 nodes. 
in this case, you will run out of memory. 

//you can use iterative dfs for this case. 

does dfs on one level at a time. 

so it visits all 1000 nodes in level 1 first. and then goes to level 2. 
it

procedure IDDFS(root)
    for depth from 0 to 3
        found ← DLS(root, depth)
        if found ≠ null
            return found

procedure DLS(node, depth)
    if depth = 0 and node is a goal
        return node
    else if depth > 0
        foreach child of node
            found ← DLS(child, depth−1)
            if found ≠ null
                return found
    return null





        
    
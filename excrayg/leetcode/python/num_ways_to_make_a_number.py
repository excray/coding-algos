# first:
# Given a number n, write the number of ways of using 1,5,10,25 to add up to n.
# e.g.: given 1, there's only one way [[1]]; given 5 there's two way: [[5], [1,1,1,1,1]]
# given 10, there's four way: [[10], [5,5], [5,1,1,1,1,1], [1,1,...1]]


# second:
# A pole of infinite length is planted vertically on the ground. 
# A stone is placed at a distance of 'd1' meters from the pole towards the right.
# A bird is sitting on the ground exactly in the middle of the pole and stone. 
# The bird flies away towards the right in such a manner that its distance from the pole and the distance between the bird and the stone at any point of time is always equal.
# Calculate the distance between the bird and it's starting point after n seconds if the bird is covering 'd2'metres horizontally every second.
# the state of the function is like: double cal(int d1, int d2, int n); you can assume d1 > 0, d2 > 0, n > 0

#  |
#  |
#  |    b     s
#  -----d1----

# third:
# given two linked list, return their first common node. if not exists, return NULL.


#try to do it recursively and then change it to dynamic programming.

c = [1,5,10,25]

def num_way(n, s):
    global c
    if n < 0 or s > 3:
        return 0
        
    if n == 0:
        return 1
        
    num_ways = 0
    t = len(c)
    
    while s < t:
        i = c[s]
        num_ways += num_way(n-i, s+1) + num_way(n, s+1)
        s+=1
        
    return num_ways
    
print(num_way(10, 0))

#third, find common node 
#find length of two lists
#increment longer list until len = shorter list
#then increment one step at a time
class node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
def print_list(node):
    temp = node
    while temp != None:
        print temp.val,
        print "->",
        temp = temp.next
    print "None" 
    
n = 7
n_list = list(range(n))

for i in range(n):
    n_list[i] = node(i)
    if i != 0:
        n_list[i-1].next = n_list[i]
    
n_list[n-1].next = None


    



     
        
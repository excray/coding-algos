class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    
    #COST = [4, 2, 4, 11] gas = [1, 4, 1, 20]
    # S = 2
    # 
    def canCompleteCircuit(self, gas, cost):
        # write your code 
        sum_rem = 0
        i = 0
        start = -1
        first = True
        notFound = False
        counter = 0
        while i != start and i < len(gas) and counter < 2*len(gas):
            # print(i, start)
            counter+=1
            if sum_rem + gas[i] < cost[i]:
                first = True
                i+=1
                if start == len(gas)-1:
                    notFound = True
                    break
            else:
                sum_rem += gas[i] - cost[i]
                if first:
                    first = False
                    start = i
                i+=1
                if i == len(gas):
                    i = 0
         
                   
        
        if i == len(gas) or notFound or counter==2*len(gas):
            return -1
            
        return start

a=[5,0,9,4,3,3,9,9,1,2]
b=[6,7,5,9,5,8,7,1,10,5]

s = Solution()
s.canCompleteCircuit(a,b)
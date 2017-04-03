class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        #num_str = "".join(num)
        k = len(num)
        if k == 0 or k==1:
            return num
           
        while k > 0:
            if int(num[k-1]) < int(num[-1]):
                break
            k-=1
            
        if k == 0:
            return sorted(num)
        
        num[k-1], num[-1] = num[-1], num[k-1]
        return num[:k]+num[k:]


s = Solution()
t=s.nextPermutation([1,3,2,3])
print(t)
s.nextPermutation([4,3,2,1])
print(t)

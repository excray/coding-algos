class Solution: 
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        
        n = len(num)
        if n == 0:
            return ""
        idxs = list(range(n)) 
        m = -1
        for i in num:
            m = max(m, i)
        mult = 1
        while m>=10:
            mult *= 10
            m/=10
        
        for i in range(n):
            p_10 = 10**int(math.log(num[i], 10))
            mult1 = int(mult/p_10)
            num[i] *= mult1
            idxs[i] = mult1
        
            
        sorted_num = sorted(enumerate(num), key=lambda x: x[1], reverse=True)
        print(sorted_num)
        new_str = ""
        for idx, val in sorted_num:
            val /= idxs[idx]
            new_str += str(int(val))
            
        return new_str
import math
s = Solution()
t=s.largestNumber([1,23,20,4,8])
print(t)

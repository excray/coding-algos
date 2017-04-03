class Solution:
    #@param num: A list of non negative integers
    #@return: A string
    #23 > 20
    # 1 > 10
    # 2 > 10
    # 20 > 1
    def is_greater_than(self, a, b):
        
        _a = []
        _b = []
        a1 = a
        b1 = b

        if not a:
            _a.append(0)
        if not b:
            _b.append(0)

        while a:
            _a.append(a%10)
            a=int(a/10)
        while b:
            _b.append(b%10)
            b=int(b/10)

        t, u = len(_a)-1, len(_b)-1
        if t == u:
            if a1 > b1:
                return True
            return False
            
        while t>=0 and u>=0:
            if _a[t] > _b[u]:
                return True
            elif _a[t] < _b[u]:
                return False

            t-=1
            u-=1

        if t == -1:
            return True

        return False
            
    
    def merge(self, l, r):
        nl = len(l)
        nr = len(r)
        temp = []
        i = 0 
        j = 0
        while i < nl and j < nr:
            if self.is_greater_than(l[i], r[j]):
                temp.append(l[i])
                i+=1
            else:
                temp.append(r[j])
                j+=1
                
        if i == nl:
            temp.extend(r[j:])
        else:
            temp.extend(l[i:])
            
        return temp
    
    def merge_sort(self, num, lo, hi):
        # print(lo, hi)
        if lo >= hi:
            return [num[lo]]
            
        m = lo+int((hi-lo)/2)
        left = self.merge_sort(num, lo, m)
        right = self.merge_sort(num, m+1, hi)

        # print(left,right)
        
        return self.merge(left, right)
    
    def largestNumber(self, num):
        # write your code here

        n = len(num)
        if n == 0:
            return ""
        
        num = self.merge_sort(num, 0, len(num)-1)

        t = sum(num)
        if t == 0:
            return "0"
        print(num)
        return ''.join(map(str, num))

s = Solution()
l = [41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]

k = s.largestNumber(l)
print(k)
        

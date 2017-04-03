class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        # write your code here  
        l_l = []
        l = []
        self.combine_h(n, 0, k, l, l_l)
        return l_l
        
    def combine_h(self, n, index, k, l, l_l):
        if index == n:
            if len(l) != 0:
                l_l.append(list(l))
                # print(l_l)
            return
            
        if k == 0:
            if len(l) != 0:
                l_l.append(list(l))
                # print(l_l)
            return
        
        l.append(index+1)
        self.combine_h( n, index+1, k-1, l, l_l)
        l.pop()
        
        self.combine_h( n, index+1, k, l, l_l)
        
        return

s = Solution()
print(s.combine(2, 1))
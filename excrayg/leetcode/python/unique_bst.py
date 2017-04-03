class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        t = []
        self.numTrees_helper(0, n, n, 0, t)
        return len(t)
        
    def numTrees_helper(self, lo, hi, total, count, t):
        if lo >= hi:
            return None
        for i in range(lo, hi):
            count += 1
            self.numTrees_helper(lo, i, total, count, t)
            self.numTrees_helper(i+1, hi, total, count, t)
            if count == total:
            	t.append(1)

        return None
            
s = Solution()
t = s.numTrees(0)
print(t)
t = s.numTrees(1)
print(t)
t = s.numTrees(2)
print(t)
t = s.numTrees(3)
print(t)




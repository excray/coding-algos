class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        if n == 0 or n == 1:
            return True
        canReach = [False]*n
        canReach[-1] = True
        i = n-2
        while i >= 0:
            if i + A[i] >= n:
                canReach[i] = True
            elif canReach[i+A[i]] == True:
                canReach[i] = True
            else:
                canReach[i] = False
                
            i-=1
            
        return canReach[0]

s = Solution()
print(s.canJump([3,2,1,0,4]))

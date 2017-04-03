class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)
        if n == 0:
            return 0
        table = [ [0]*(n+1) for i in range(n+1) ]
        for length in range(1, n+1):
            s = 0
            e = length
            while s+length <= n:
                if A[s:e] == A[s:e][::-1]:
                    table[s][e] = 0
                else:
                    table[s][e] = min(table[s][e-1], table[s+1][e]) + 1
                
                s+=1
                e+=1
        from pprint import pprint
        pprint(table) 
        return table[0][n]

s=Solution()
print(s.minCut("ababb"))
print(s.minCut("AB"))


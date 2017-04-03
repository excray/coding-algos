class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        return self.h(A, 0, B, 0, C, 0, {})
        
    def h(self, A, a, B, b, C, c, d):
        
        if (a,b) in d:
            return d[(a,b)]

        # print(A[a:], B[b:], C[c:])
          
        if a == len(A):
            if B[b:] == C[c:]:
                # print("hi")
                return True
            else:
                return False
        
        if b == len(B):
            if A[a:] == C[c:]:
                return True
            else:
                return False
        
        with_a = False   
        if A[a] == C[c]:
            with_a = self.h(A, a+1, B, b, C, c+1, d)
        
        with_b = False
        if not with_a and B[b] == C[c]:
            with_b = self.h(A, a, B, b+1, C, c+1, d)
            
            
        d[(a,b)] = with_a or with_b
        return d[(a,b)]  
        

A="eZCHXr0CgsB4O3TCDlitYI7kH38rEElI"
B="UhSQsB6CWAHE6zzphz5BIAHqSWIY24D"
C="eUZCHhXr0SQsCgsB4O3B6TCWCDlAitYIHE7k6H3z8zrphz5EEBlIIAHqSWIY24D"

s = Solution()    
print(s.isInterleave(A,B,C))    
        

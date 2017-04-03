class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        n = len(s1)
        m = len(s2)
        
        # mat = [[False] * m+1 for i in range(n+1)]
        
        
        return self.ih( s1, 0, s2, 0, s3, 0)
        
    def ih(self, s1, i, s2, j, s3, k):
        print(i,j,k)
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
            
        if k == len(s3):
            return False
            
        if i == len(s1) and j == len(s2):
            return False
            
        if i == len(s1):
            if s2[j] == s3[k]:
                return self.ih(s1, i, s2, j+1, s3, k+1)
            else:
                return False
            
        elif j == len(s2):
            if s1[i] == s3[k]:
                return self.ih(s1, i+1, s2, j, s3, k+1)
            else:
                return False
        
        else:
            if s1[i] == s2[j] and s1[i] == s3[k]:
                return self.ih(s1, i+1, s2, j, s3, k+1) or self.ih(s1, i, s2, j+1, s3, k+1)
            elif s1[i] == s3[k]:
                return self.ih(s1, i+1, s2, j, s3, k+1)
                
            elif s2[j] == s3[k]:
                return self.ih(s1, i, s2, j+1, s3, k+1)
            
            else:
                return False

s = Solution()
a = "aabcc"
b = "dbbca"
s_t = "aadbbcbcac"
s_f = "aadbbbaccc"
print(s.isInterleave(a,b,s_t))
print(s.isInterleave(a,b,s_f))

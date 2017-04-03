class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        n = len(A)
        if n == 0:
            return ""
        A = list(A)
        idxs = [1]*n
        sorted_str = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
        for i in range(k):
            idxs[sorted_str[i][0]] = 0
        r = ""
        for i,v in enumerate(A):
            if idxs[i] == 1:
                r+=v
                
        return r

s = Solution()
A="178542"
k=4
print(s.DeleteDigits(A,k))

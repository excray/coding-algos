class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.

        D = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        R = {}
        for k,v in D.items():
            R[v] = k
            
        rules = [["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"]]
        for rule in rules:
            s, f1, f2 = rule
            num = R[f1] - R[s]
            D[num] = s+f1
            num = R[f2] - R[s]
            D[num] = s+f2
            
        s = ""
        curr_mod = 10
        T  = A
        while T != 0:
            rem = A % curr_mod
            A -= rem
            T = int(A/curr_mod)
            print(rem, T)

            curr_mod *= 10
            if rem in D:
                s=D[rem]+s
            elif rem / 1000 >= 1:
                s=D[1000]*(rem/1000)+s
            elif rem / 500 >= 1:
                s=D[500]*(rem/500)+s
            elif rem / 100 >= 1:
                s=D[100]*(rem/100)+s
            elif rem / 50 >= 1:
                s=D[50]*(rem/50)+s
            elif rem / 10 >= 1:
                s=D[10]*(rem/10)+s
            elif rem / 5 >= 1:
                s=D[5]*(rem/5)+s
            elif rem / 1 >= 1:
                s=D[1]*(rem/1)+s
            
        return s
        
s = Solution()
print(s.intToRoman(41))
        
        
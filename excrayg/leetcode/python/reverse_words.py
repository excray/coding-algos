class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        if s == "":
            return s
        r = s[::-1]
        si = 0
        spaceFound = False
        r = list(r)
        n = len(r)
        ei = 0
        while ei < n:
            if r[ei] == " ":
                if spaceFound:
                    del r[ei]
                    n-=1
                    continue
                else:
                    spaceFound = True
                    self.reverseWord(r, si, ei)
            else:
                if spaceFound:
                    si = ei
                    spaceFound = False
            ei+=1
            
        print(r, si)
        self.reverseWord(r, si, len(r)-1) 
            
        return "".join(r)
        
    def reverseWord(self, r, si, ei):
        if si <= ei:
            return r
        else:
            temp = r[si]
            r[si] = r[ei]
            r[ei] = temp
            print(r)
            return self.reverseWord(r, si+1, ei-1)


s = Solution()
print(s.reverseWords("hi!"))
class Solution(object):
    
    def h(self, s, start_idx, l, ll):
        if start_idx == len(s):
            ll.append(list(l))
        else:
            for idx in range(start_idx, len(s)):
                cand = s[start_idx:idx+1] 
                if cand == cand[::-1]:
                    l.append(cand)
                    self.h(s, idx+1, l, ll)
                    l.pop()
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        l = []
        ll = []
        self.h(s, 0, l, ll)
        return ll

s = Solution()
print(s.partition("abc"))
print(s.partition("aab"))

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "" and p == "":
            return True
        
        if p == "" or  s == "":
            return False
            
        char_in_str, rest_char_in_str = s[0], s[1:]
        char_in_pat, rest_char_in_pat = p[0], p[1:]
        
        if char_in_str == char_in_pat or char_in_pat == '?':
            return self.isMatch(rest_char_in_str, rest_char_in_pat)

        if char_in_pat == '*':
            n = len(s)
            for i in range(n):
                if self.isMatch(s[i:], rest_char_in_pat):
                    return True

            return self.isMatch(s, rest_char_in_pat)
            
        return False


s = Solution()
print(s.isMatch("aa","a"))

print(s.isMatch("aa","aa"))
print(s.isMatch("aaa","aa"))

print(s.isMatch("aa", "*"))
print(s.isMatch("aa", "a*"))

print(s.isMatch("ab", "?*"))
print(s.isMatch("aab", "c*a*b"))

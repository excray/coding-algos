class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 0
            
        st = []
        dict.add(end)
        st.append(start)
        l = 1
        visited = set()
        cand = self.ch(dict)
        nl = 0
        cl = 1
        while len(st) != 0:
            node = st[0]
            st = st[1:]

            print(node)
            
            if node == end:
                return l
            
            visited.add(node)
            neighbours = self.gn(node, dict, cand)
            print(node, neighbours)
            for n in neighbours:
                if n not in visited:
                    if end == n:
                        l+=1
                        return l
                    else:
                        st.append(n)
                    nl+=1
            cl-=1
            if cl == 0:
                cl = nl
                nl = 0
                l+=1
            # l+=1
        return l
    
    def gn(self, node, dict, cand):
        neigh = set()
        for i in range(1,len(node)+1):
            idx = i-1
            lts = cand[i]
            for j in lts:
                if node[idx] != j:
                    t = list(node)
                    t[idx] = j
                    new_node = "".join(t)
                    if new_node in dict:
                        neigh.add(new_node)
        return neigh
        
    def ch(self, d):
        cand = dict() 
        for w in d:
            for i,c in enumerate(w):
                idx = i+1
                if idx not in cand:
                    cand[idx] = set()
                cand[idx].add(c)
        return cand

s = Solution()
print(s.ladderLength("game", "thee", {"frye","heat","tree","thee","game","free","hell","fame","faye"}))

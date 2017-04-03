class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(list(valuelist))
        prev = None
        for i in range(start, length):
            if target < candidates[i]:
                break
            # if prev != None and prev == candidates[i]:
            #     continue
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
            prev = candidates[i]
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        c = set(candidates)
        candidates = []
        for i in c:
            candidates.append(i)
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


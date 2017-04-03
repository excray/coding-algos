class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        
        if beginWord == endWord:
            return []

        dict1 = set()
        for w in wordList:
            dict1.add(w)
            
        dict1.add(beginWord)
        dict1.add(endWord)
        wordSeq = dict()

        for k, v in dict1.items():
            wordSeq[k] = []

        self.do_bfs(beginWord, endWord, wordList, wordSeq)
        
        return wordSeq
        
    def get_neigh(self, word, wordList, visited):
        neigh = []
        for idx in range(len(word)):
            for c in range(ord('a'), ord('z')+1):
                new_word = word[0:idx]+chr(c)+word[idx+1:]
                # print(new_word)
                if (new_word in wordList) and (new_word not in visited) and (new_word != word):
                    neigh.append(new_word)
                    
        return neigh
        
    def do_bfs(self, beginWord, endWord, wordList, wordSeq):
        queue = []
        visited = set()
        queue.append(beginWord)
        short_seq = []

        
        while len(queue) != 0:
            # while seq_left:
            word = queue.pop(0)
            neighbours = self.get_neigh(word, wordList, visited)
            queue.extend(neighbours)
            short_seq.append(word)
            visited.add(word)

            if word == endWord:
                # print(short_seq, queue)
                min1 = min(min1, len(short_seq))
                # if len(short_seq) != min1:
                #     seq_left = False
                #     break
                wordSeq.append(short_seq)
            
        return
            

beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]
s = Solution()
t = s.findLadders(beginWord, endWord, wordList)
print(t)











class Solution:
     # param Start, a String 
    # param End, a String 
    # param dict, a set of String 
    # return a List of lists of String 
    def findLadders (self, Start, End, dict):
         def buildpath ( path, Word):
             if len (prevMap [Word]) == 0:
                path.append (Word); currPath = path [:]
                currPath.reverse (); result.append (currPath)
                path.pop ();
                return
            path.append (word)
            for iter in prevMap [Word]:
                buildpath (path, iter)
            path.pop ()
        
        result = []
        prevMap = {}
        length = len (Start)
         for i in dict:
            prevMap [i] = []
        candidates = [set (), set ()]; current = 0; Previous = 1
        candidates [current] .add (start)
        while True:
            current, Previous = Previous, current
             for i in candidates [Previous]: dict.remove (i)
            candidates [current] .clear ()
            for Word in candidates [Previous]:
                 for i in range (length):
                    part1 = Word [: i]; part2 = Word [i + 1 :]
                     for J in  ' abcdefghijklmnopqrstuvwxyz ' :
                         if Word [i] =! J:
                            nextword = J + part1 + part2
                             if nextword in dict:
                                prevMap [nextword] .append (word)
                                candidates [current] .add (nextword)
            if len (candidates [current]) == 0: return result
             if End in candidates [current]: break
        buildpath ([], end)
        return result
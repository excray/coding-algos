class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        # if n < 4:
        #     return []
        cols = [-100] * n
        cur_row = 0
        solns = []
        self.sh(n, cur_row, cols, solns)
        return solns
        
    def can_be_placed(self, i, cur_row, cols):
        if cur_row == 0:
            return True
            
        t = cur_row-1
        d = 1
        while t >= 0:
            print(cols[t], i, t)
            if abs(cols[t]-i) == d:
                return False
            d+=1
            t-=1
        
        t = cur_row
        # print(t)
        while t >= 0:
            if cols[t] == i:
                return False
            t-=1
            
        return True

    def fs(self, cols):
        n = len(cols)
        l = ["."] * n
        q = "Q"
        t = []
        for i in cols:
            l[i] = "Q"
            t.append("".join(l))
            l[i] = "."

        return t
        
    def sh(self, n, cur_row, cols, solns):
        
        if cur_row == n:
            solns.append(self.fs(cols))
            return
        
        for i in range(n):
            if self.can_be_placed(i, cur_row, cols):
                print(cur_row, i)
                cols[cur_row] = i
                self.sh(n, cur_row+1, cols, solns)
                cols[cur_row] = -100
        
        return 

s = Solution()
print(s.solveNQueens(4))
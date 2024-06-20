class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        self.search(n, [], results)
        return results
    
    def search(self, n, cols, results):
        row = len(cols)
        if row == n:
            results.append(self.printboard(cols))
            return 
        for col in range (n):
            if not self.isValid(cols, col, row):
                continue
            cols.append(col)
            self.search(n, cols, results)
            cols.pop()
            
    def isValid(self, cols, col, row):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r + c == col+row or r - c == row - col:
                return False
        return True
    
    def printboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j ==cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
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
            results.append()
            return 
        for col in range (n):
            if not self.isValid(cols, col, row):
                continue
            cols.append(col)
            self.search(n, cols, results)
            cols.pop()
            
    def isValid(cols, col, row):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r + c == col+row or r - c == col - row:
                return False
        return True
    
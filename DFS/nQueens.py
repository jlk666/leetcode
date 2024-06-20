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
        if n == len(cols):
            return results
        
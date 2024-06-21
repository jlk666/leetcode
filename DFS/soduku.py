class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        used = self.initialUsed(board)
        self.dfs(used,0,board)
        
    #step 1 store the information from board to used sets
    def initialUsed(self, board):
        used = { 
            'row': [set() for _ in range(9)],
            'column':[set() for _ in range(9)],
            'block':[set() for _ in range(9)],
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue 
                
                used['row'][i].add(board[i][j])
                used['column'][j].add(board[i][j])
                used['block'][i//3*3+j//3].add(board[i][j])
                
        return used
    
    def isValid(self, i,j,val,used):
        if val in used['row'][i]:
            return False
        if val in used['column'][j]:
            return False
        if val in used['block'][i//3*3+j//3]:
            return False
        return True 
    
    def dfs(self, used, index, board):
        if index == 81:
            return True
        i = index // 9
        j = index % 9 
        
        if board[i][j] != '.':
            return self.dfs(used, index + 1, board)
        
        for val in range(1, 10):
            if not self.isValid(i,j, val, used):
                continue
            board[i][j] = val
            used['row'][i].add(val)
            used['column'][j].add(val)
            used['block'][i//3*3+j//3].add(val)
            
            if self.dfs(used, index + 1, board):
                return True
            
            used['block'][i//3*3+j//3].remove(val)
            used['column'][j].remove(val)
            used['row'][i].remove(val)
            board[i][j] = '.'
            
        return False
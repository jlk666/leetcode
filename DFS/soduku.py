class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
    #step 1 store the information from board to used sets
    def initialUsed(self, board):
        used = { 
            ['row']: [set() for _ in range(9)],
            ['column']:[set() for _ in range(9)],
            ['block']:[set() for _ in range(9)],
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == ',':
                    continue 
                
                used['row'][i].add(board[i][j])
                used['column'][j].add(board[i][j])
                used['block'][i//3*3+j//3].add(board[i][j])
                
        return used
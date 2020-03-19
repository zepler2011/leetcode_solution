class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue 
                elif board[i][j] not in '123456789':
                    return False
                else:
                    if board[i][j] not in r[i]:
                        r[i].add(board[i][j])
                    else:
                        return False 
                    
                    if board[i][j] not in c[j]:
                        c[j].add(board[i][j])
                    else:
                        return False
                    
                    if board[i][j] not in grid[3*(i//3)+j//3]:
                        grid[3*(i//3)+j//3].add(board[i][j])
                    else:
                        return False
                    
        return True
        
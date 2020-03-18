class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        r = [set()] * 9
        c = [set()] * 9
        b = [[0] * 3  for _ in range(3)]
        for i in range(3):
            for j in range(3):
                b[i][j] = set()
        
        for i in range(9):
            exist = set(board[i])
            for d in range(1, 9):
                if d not in exist:
                    r[i].add(d)

        for j in range(9):
            exist = [board[i][j] for i in range(9)]
            for d in range(1, 9):
                if d not in exist:
                    c[j].add(d)

        for i in range(3):
            for j in range(3):
                exist = []
                I = i*3
                J = j*3
                for i_ in range(3):
                    for j_ in range(3):
                        
                        if board[I+i_][J+j_] != 0:
                            exist.append(board[I+i_][J+j_])
                for d in range(1, 9):
                    if d not in exist:
                        b[i][j].add(d)

        self.dfs(board, 0, 0, r, c, b)
        return
    
    def dfs(self, board, I, J, r, c, b):
        if I == 9 and J == 9:
            return True
        
        for i in range(I, 9):
            for j in range(J, 9):

                for d in range(9):
                    if board[i][j] != 0:
                        continue
                    if d not in r[i]:
                        continue
                    if d not in c[j]:
                        continue
                    if d not in b[i%3][j%3]:
                        continue 
                    
                    r[i].remove(d)
                    c[j].remove(d)
                    b[i%3][j%3].remove(d)
                    board[i][j] = d
                    if self.dfs(board, i, j, r,c,b):
                        return True
                    board[i][j] = 0
                    r[i].add(d)
                    c[j].add(d)
                    b[i%3][j%3].add(d)
                    
        return False

"""
思路：用三个hashset 分别代表 能否 加入的 数字
在dfs时候 仅当 能够 使用时才可以选当前数字
"""


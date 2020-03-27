class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # 在board上面的dfs
        # 如果 match，就继续
        # 四个方向search，用visited 防止回流/成环
        # 只要 pattern 为空，表明找到了，返回True
        
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        return self.dfs(board, 0, 0, word, set())
    
    def dfs(self, B, i, j, pattern, visited):
        
        # 思考：到这里以后，pattern的第一个子，已经match了，还是没有match?
        #   已经在上一级match过了，在这里是要找 i,j得下一个，谁跟pattern[0] 一样
        
        for i in range(len(B)):
            for j in range(len(B[0])):
                if pattern[0] != B[i][j]:
                    continue
                    
                if (i,j) in visited:
                    continue
                    
                visited.add((i,j))
                if self.helper(B, i,j, pattern[1:], visited):
                    return True
                visited.remove((i,j))
                
        return False

    
    def helper(self, B, i,j, pattern, visited):
        if not pattern:
            return True
        
        for delta_i,delta_j in self.directions:
            i_ = i+delta_i
            j_ = j+delta_j
            
            if (i_, j_) in visited:
                continue 
                
            if i_<0 or i_>len(B)-1 or j_<0 or j_>len(B[0])-1:
                continue
                
            if pattern[0] != B[i_][j_]:
                continue 
                
            visited.add((i_,j_))
            if self.helper(B, i_,j_, pattern[1:], visited):
                return True
            visited.remove((i_,j_))
        return False
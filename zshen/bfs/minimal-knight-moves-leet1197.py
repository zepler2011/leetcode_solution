class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        if x==0 and y==0:
            return 0
        
        q1,q2 = [(0,0)],[]
        forward = {(0,0):0}
        
        q3,q4 = [(x,y)],[]
        backward = {(x,y):0}
        
        DIRECTIONS = [(1,2),(2,1),(2,-1),(1,-2),(-2,-1),(-1,-2),(-1,2),(-2,1)]
        
        
        while q1 or q3:
            if q1:
                x,y = q1.pop(0)
                for dx,dy in DIRECTIONS:
                    x_ = x+dx
                    y_ = y+dy
                    if (x_,y_) in forward:
                        continue 
                    q2.append((x_,y_))
                    forward[(x_,y_)] = forward[(x,y)] + 1 
                    if (x_,y_) in backward:
                        return forward[(x_,y_)] + backward[(x_,y_)]
                    
            if q3:
                x,y = q3.pop(0)
                for dx,dy in DIRECTIONS:
                    x_ = x + dx
                    y_ = y + dy 
                    if (x_,y_) in backward:
                        continue 
                    q4.append((x_,y_))
                    backward[(x_,y_)] = backward[(x,y)] + 1
                    if (x_,y_) in forward:
                        return forward[(x_,y_)] + backward[(x_,y_)]
                    
            if not q1 and not q3:
                q1,q2 = q2,q1
                q3,q4 = q4,q3
                
                
        return -1 
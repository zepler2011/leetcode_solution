"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        memo = {}
        return self.rob(root, memo)

    def rob(self, node, memo):
        if not node:
            return 0
            
        if node in memo:
            return memo[node]
            
        s1 = 0
        s1 += self.rob(node.left, memo) + self.rob(node.right, memo)
        
        s2 = node.val
        if node.left:
            s2 += self.rob(node.left.left, memo) + self.rob(node.left.right, memo)
        if node.right:
            s2 += self.rob(node.right.left, memo) + self.rob(node.right.right, memo)
        
        money = max(s1, s2)
        memo[node] = money
        return money

"""
two cases:
1. do not include node it self, then get sum of sons
2. include node itself, then get sum of grand children

optimization:
use memoization search
"""
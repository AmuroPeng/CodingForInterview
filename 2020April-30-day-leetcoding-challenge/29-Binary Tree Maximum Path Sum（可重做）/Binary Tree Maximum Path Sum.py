# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_sum(self, root: TreeNode):
        if root == None: return 0
        val = root.val
        sum_l = max(0, self.dfs_sum(root.left))
        sum_r = max(0, self.dfs_sum(root.right))
        self.ans = max(self.ans, sum_l + sum_r + val)
        return  max(sum_l , sum_r) + val
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = - 1e9
        self.dfs_sum(root)
        return self.ans

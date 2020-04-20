# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: list) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(8)
    p = root
    p.left = TreeNode(5)
    p = p.left
    p.left = TreeNode(1)
    p.right = TreeNode(7)
    p = root
    p.right = TreeNode(10)
    p = p.right
    p.right = TreeNode(12)
    print(root == s.bstFromPreorder([8, 5, 1, 7, 10, 12]))

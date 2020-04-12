# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getDepth(root, depth):
            if root.left and root.right:
                return max(getDepth(root.left, depth), getDepth(root.right, depth))
            elif root.left:
                depth += 1
                return getDepth(root.left, depth)+1
            elif root.right:
                depth += 1
                return getDepth(root.right, depth)+1
            else:
                return 1
        return getDepth(root, 0)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode('1')
    root.left = TreeNode('2')
    root.right = TreeNode('3')
    root.left.left = TreeNode('4')
    root.left.right = TreeNode('5')
    print(s.diameterOfBinaryTree(root))

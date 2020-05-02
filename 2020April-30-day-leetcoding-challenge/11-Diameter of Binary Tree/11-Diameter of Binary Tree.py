# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_ = 0

        def getDepth(root, depth):
            depth += 1
            if root.left and root.right:
                self.max = max(getDepth(root.left, depth) +
                               getDepth(root.right, depth), self.max_)
                return max(getDepth(root.left, depth),
                           getDepth(root.right, depth))
            elif root.left:
                return getDepth(root.left, depth)
            elif root.right:
                return getDepth(root.right, depth)
            else:
                return depth
        return max(getDepth(root, 0), self.max_)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode('1')
    root.left = TreeNode('2')
    root.right = TreeNode('3')
    root.left.left = TreeNode('4')
    root.left.right = TreeNode('5')
    print(s.diameterOfBinaryTree(root))

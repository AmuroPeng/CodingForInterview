# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def digui(self, root, depth):
        print(type(root.val))
        print(type(self.x))
        if root.left.val + root.right.val == self.x+self.y:
            self.x_depth = 100
            self.y_depth = 1000
            return
        if root.left == None:
            return
        else:
            if root.left == self.x:
                self.x_depth = depth
            elif root.left == self.y:
                self.y_depth = depth
            self.digui(root.left,depth+1)
        if root.right == None:
            return
        else:
            if root.right == self.x:
                self.x_depth = depth
            elif root.right == self.y:
                self.y_depth = depth
            self.digui(root.right,depth+1)
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_depth = 0
        self.y_depth = 0
        # self.depth = 1
        self.x = x
        self.y = y
        depth = 1
        self.digui(root,depth)
        return self.x_depth==self.y_depth
            
if __name__ == "__main__":
    s=Solution()
    root = TreeNode(1)
    print(s.isCousins(root,1,2))
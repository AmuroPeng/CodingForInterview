# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return 1
        # self.dict_ = dict(int)
        # self.dict_[root.val] += 1
        # self.xor = root.val
        set_ = {root.val}
        xor = root.val
        self.result = 0
        self.digui(root, set_, xor)
        return self.result

    def digui(self, root, set_, xor):
        print(set_)
        if root.left:
            # xor = xor ^ root.left.val
            if root.left.val in set_:
                set_.remove(root.left.val)
            else:
                set_.add(root.left.val)
            print(set_)
            self.digui(root.left, set_, xor)
        if root.right:
            # xor = xor ^ root.right.val
            if root.right.val in set_:
                set_.remove(root.right.val)
            else:
                set_.add(root.right.val)
            print(set_)
            self.digui(root.right, set_, xor)
        if root.left == None and root.right == None:
            print(f"end",set_)
            if len(set_) == 1:
                self.result += 1
            return
        return


if __name__ == "__main__":
    pass
    s = Solution()

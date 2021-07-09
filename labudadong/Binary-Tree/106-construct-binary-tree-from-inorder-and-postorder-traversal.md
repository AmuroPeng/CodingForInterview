
## 题目地址(106. Construct Binary Tree from Inorder and Postorder Traversal)

https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

## 题目描述

```
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]


Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
```

## 前置知识

- 10min 05302021

## 公司

- 暂无

## 思路

## 关键点

1. 对于任意一颗树而言，后序遍历的形式总是
[ [左子树的前序遍历结果], [右子树的前序遍历结果]， 根节点 ]
2. 即根节点总是前序遍历中的第一个节点。而中序遍历的形式总是
[ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果] ]

## 代码

- 语言支持：Java

Java Code:

```java

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (postorder.length == 0) return null;
        if (inorder.length == 0) return null;
        TreeNode root = new TreeNode(postorder[postorder.length - 1]);
        int sub_root_idx = 0;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == postorder[postorder.length - 1]) sub_root_idx = i;
        }
        root.left = buildTree(Arrays.copyOfRange(inorder, 0, sub_root_idx), Arrays.copyOfRange(postorder, 0, sub_root_idx));
        root.right = buildTree(Arrays.copyOfRange(inorder, sub_root_idx + 1, inorder.length), Arrays.copyOfRange(postorder, sub_root_idx, postorder.length - 1));
        return root;
    }
}

```


**复杂度分析**

令 n 为数组长度。

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$



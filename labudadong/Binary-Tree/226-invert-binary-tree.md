
## 题目地址(226. 翻转二叉树)

https://leetcode-cn.com/problems/invert-binary-tree/

## 题目描述

```
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]


Example 2:

Input: root = [2,1,3]
Output: [2,3,1]


Example 3:

Input: root = []
Output: []


 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

## 耗时

- 08:30

## 公司

- 暂无

## 思路

## 关键点

-  

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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        TreeNode left_node = root.left;
        TreeNode right_node = root.right;
        root.right = invertTree(left_node);
        root.left = invertTree(right_node); 
        return root;        
    }
}

```


**复杂度分析**

令 n 为数组长度。

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$



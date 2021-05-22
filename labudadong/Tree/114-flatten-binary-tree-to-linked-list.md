
## 题目地址(114. Flatten Binary Tree to Linked List)

https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

## 题目描述

```
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

 

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]


Example 2:

Input: root = []
Output: []


Example 3:

Input: root = [0]
Output: [0]


 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
```

## 前置知识

- 20min

## 公司

- fail 05232021

## 思路

- 后序遍历
- 递归


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
    public void flatten(TreeNode root) {
        if(root==null)  return;
        flatten(root.left); //将根节点的左子树变成链表
        flatten(root.right); //将根节点的右子树变成链表
        TreeNode temp = root.right; //保存树的右子树
        root.right = root.left;   //将根的右子树换成左边的链表 
        root.left = null; //左子树置空
        while(root.right!=null)   root = root.right; //找到右子树最右边一个节点
        root.right = temp; //把右边链表接到右子树最右边那个节点
    }
}


```


**复杂度分析**

令 n 为数组长度。

- 时间复杂度：$O(n)$
- 空间复杂度：$O(1)$



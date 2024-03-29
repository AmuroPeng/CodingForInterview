
## 题目地址(116. Populating Next Right Pointers in Each Node)

https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

## 题目描述

```
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}


Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
```

## 前置知识

- 24:13

## 公司

- 暂无

## 思路

- 层次遍历（BFS）
- DFS也可以做，感觉更简单

## 关键点

-  队列Queue是否为空 写法：queue.isEmpty()

## 代码

- 语言支持：Java

Java Code:

```java

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null) return root;
        Queue<Node> queue = new LinkedList<Node>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size != 0) {
                Node node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                    queue.offer(node.right);
                }
                size--;
                if (size != 0) node.next = queue.peek();
                else node.next = null;
            }
        }
        return root;
    }
}

```


**复杂度分析**

令 n 为数组长度。

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$



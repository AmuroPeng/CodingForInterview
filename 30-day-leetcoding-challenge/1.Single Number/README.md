# 01-Single Number
# 
-----------
# 题目链接
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/

# 题目描述
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

# 复杂度
O(n)

# 思路
1. hash
2. 使用异或XOR，1和2异或的本质是按位异或，所以只要是两个重复就可以异或为0，单数的则会最后显示。所以以后**遇到单双个数问题，可以使用异或**

0+0
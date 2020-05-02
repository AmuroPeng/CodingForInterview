# 02-Happy Number
# 
-----------
# 题目链接
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

# 题目描述
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

# 复杂度
O(n)

# 思路
1. 练习递归，但是需要考虑无限循环情况要return False，所以需要记录每次的结果
2. 检测是否存在循环->可以考虑用快慢指针->可以节省空间，没必要再建一个dict存结果
3. 可以用set代替dict，set只有不可重复的key值，没有value

0+0
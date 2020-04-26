# Longest Common Subsequence
# 
-----------
# 题目链接
https://leetcode.com/problems/longest-common-subsequence/

# 题目描述
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

# 复杂度
1. 时间复杂度 O()
2. 空间复杂度 O()

# 思路
1. **二维动态规划**:这种题的思路是**从边界出发，通过状态转移方程求解状态**
2. 只要涉及`子序列`问题，十有八九都需要动态规划来解决.因为子序列类型的问题，穷举出所有可能的结果都不容易，而动态规划算法做的就是穷举 + 剪枝，它俩天生一对儿。
3. https://leetcode-cn.com/problems/longest-common-subsequence/solution/marvelzhong-deng-de-xue-xi-bi-ji-1143-by-tyanyon-2/

0+0
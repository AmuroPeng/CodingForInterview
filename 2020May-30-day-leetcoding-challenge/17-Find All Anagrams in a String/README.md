# 438. Find All Anagrams in a String
# 
-----------
# 题目链接
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

# 题目描述
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

# 复杂度
1. 时间复杂度 O()
2. 空间复杂度 O()

# 思路
1. 滑动窗口：双指针
2. 先把窗口放上去，不管符不符合先去做个差，然后每次滑动并且维护窗口（更新这个差值），直到差值为0即完美匹配到
3. 大佬的滑动窗口技巧：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/hua-dong-chuang-kou-tong-yong-si-xiang-jie-jue-zi-/%E5%8F%8C%E6%8C%87%E9%92%88%E6%8A%80%E5%B7%A7.md

0+0
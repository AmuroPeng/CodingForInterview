# 06-Group Anagrams
# 
-----------
# 题目链接
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/

# 题目描述
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
# 复杂度
O()

# 思路
1. python中dic的key必须是可哈希的：
   > 不严谨但易懂的解释：

   > 不严谨但易懂的解释：
   > 一个对象在其生命周期内，如果保持不变，就是hashable（可哈希的）。

   > hashable ≈ imutable     可哈希 ≈ 不可变

   > 在Python中：

   > list、set和dictionary 都是可改变的，比如可以通过list.append()，set.remove()，dict['key'] = value对其进行修改，所以它们都是不可哈希的；

   > 而tuple和string是不可变的，只可以做复制或者切片等操作，所以它们就是可哈希的。

   > 原文链接：https://blog.csdn.net/qq_17753903/article/details/85345996
2. 初始化dic = collections.defaultdict(list) 意思是dict里的值是list型的，便于直接使用append
3. set是可变集合，相对应的frozenset是不可变集合

20+0
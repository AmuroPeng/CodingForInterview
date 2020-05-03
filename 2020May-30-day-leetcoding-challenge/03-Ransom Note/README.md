# Ransom Note
# 
-----------
# 题目链接
https://leetcode.com/problems/ransom-note/

# 题目描述
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

# 复杂度
1. 时间复杂度 O()
2. 空间复杂度 O()

# 思路
1. class collections.Counter([iterable-or-mapping])
Counter 集成于 dict 类，因此也可以使用字典的方法，此类返回一个以**元素为 key 、元素个数为 value 的 Counter 对象集合**

from collections import Counter
s = "hello pinsily"
d = Counter(s)
d
Counter({'l': 3, 'i': 2, 'h': 1, 'e': 1, 'o': 1, ' ': 1, 'p': 1, 'n': 1, 's': 1, 'y': 1})
2. python中 xxx.count的速度很快

0+0
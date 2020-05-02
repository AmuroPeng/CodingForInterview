# First Bad Version
# 
-----------
# 题目链接
https://leetcode-cn.com/problems/first-bad-version/solution/pythondi-yi-ge-cuo-wu-de-ban-ben-by-jutraman/

# 题目描述
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

# 复杂度
1. 时间复杂度 O(logn)
2. 空间复杂度 O(1)

# 思路
1. 二分查找
2. 

0+0
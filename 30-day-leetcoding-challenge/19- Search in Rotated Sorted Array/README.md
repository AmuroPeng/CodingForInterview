# 19- Search in Rotated Sorted Array
# 
-----------
# 题目链接
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

# 题目描述
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

# 复杂度
1. 时间复杂度 O(logn)
2. 空间复杂度 O()

# 思路
1. 二分查找：因为（至少有一半）是有序的，如果target不在这一半有序的list中，那也可以肯定一定在另一半的list中。
2. 

0+0
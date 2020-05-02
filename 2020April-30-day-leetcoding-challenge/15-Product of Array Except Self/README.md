# 15-Product of Array Except Self
# 
-----------
# 题目链接


# 题目描述
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# 复杂度
1. 时间复杂度 O(n)
2. 空间复杂度 O(n)

# 思路
1. 所有数的左边和右边 乘积和 有规律
2. 要求O(n)，又没说只能遍历一遍。。O(n+n+n)也行啊

60+0
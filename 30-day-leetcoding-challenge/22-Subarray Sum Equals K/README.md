# Subarray Sum Equals K
# 
-----------
# 题目链接


# 题目描述
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
   Hide Hint #1  
Will Brute force work here? Try to optimize it.
   Hide Hint #2  
Can we optimize it by using some extra space?
   Hide Hint #3  
What about storing sum frequencies in a hash table? Will it be useful?
   Hide Hint #4  
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

# 复杂度
1. 时间复杂度 O(n)
2. 空间复杂度 O(n)

# 思路
1. sum(i,j)=sum(j)-sum(i) 也就是说在这道题里sum(i,j)要求等于k，所以sum(i)=sum(j)-k
2. HashMap的key存sum值，value存等于该值的次数
3. 以后遇到需要`子字符串的和`，就可以将它转换成`前后两个值累加和的差`

20+60
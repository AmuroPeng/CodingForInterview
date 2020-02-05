# Array
# 
-----------
# 题目链接
https://www.nowcoder.com/questionTerminal/94a4d381a68b47b7a8bed86f2975db46

# 题目描述
给定一个数组A[0,1,...,n-1]请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

# 复杂度
O(n)

# 思路
1. ![image](https://github.com/AmuroPeng/CodingForInterview/blob/master/%E5%89%91%E6%8C%87Offer/Array/051-%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84/051-%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84.jpeg)
2. 很多相同的部分->分成两部分，可以每个部分每次多乘一个数，就是一次遍历了

10+20
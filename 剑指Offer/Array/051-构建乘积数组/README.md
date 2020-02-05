# Array
# 
-----------

# 题目描述
给定一个数组A[0,1,...,n-1]请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

# 复杂度
O(n)

# 思路
1. ![image](http://github.com/AmuroPeng/readme_add_pic/raw/master/images/nongshalie.jpg)
2. 很多相同的部分->分成两部分，可以每个部分每次多乘一个数，就是一次遍历了

10+20
# 13-Contiguous Array
# 
-----------
# 题目链接


# 题目描述
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

# 复杂度
1. 时间复杂度 O()
2. 空间复杂度 O()

# 思路
1. trick:
累积和
使用的方法是求和+hashmap的方法，首先从头开始遍历，如果当前值是0就sum-1，否则就sum+1.这样如果得到了一个sum就知道在此之前出现了1的个数和0的个数的差值。因此，当后面该sum再次出现的时候，我们就知道了这个差值再次出现，也就是说，从第一次这个差值出现和第二次这个差值出现之间0和1的个数是一样多的。

因此我们需要一个map来保存0和1的差值。如果这个差值没出现过就给它赋值为它出现的索引。我们要求的就是当同样的差值出现的时候，两者之间的最大值。另外注意，当这个差值再次出现的时候不要更新map。即我们的策略是只保存这个差值出现的第一个位置，只有这样我们才知道最长的连续子数组是多少。

这个题的官方解答里面给出了详细的每一步的变化过程，推荐一看。

也可以在刚开始的时候就把nums中的0替换成-1，这样就可以直接使用total_sum加上当地前数值即可。

需要注意的是字典应该有个初始化值，代表在刚开始的时候没有任何元素的位置是-1，否则后面出现0的时不能和最开始的位置求位置差。
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/82667054
   

0+0
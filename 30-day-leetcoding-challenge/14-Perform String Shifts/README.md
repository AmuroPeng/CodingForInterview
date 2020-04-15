# 14-Perform String Shifts
# 
-----------
# 题目链接
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/

# 题目描述
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
   Hide Hint #1  
Intuitively performing all shift operations is acceptable due to the constraints.
   Hide Hint #2  
You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.

# 复杂度
1. 时间复杂度 O(max(m,n))
2. 空间复杂度 O(1)

# 思路
1. 可以用双端队列，Python:deque([]) 
   
   - d = collections.deque([])
   - d.append('a') # 在最右边添加一个元素，此时 d=deque('a')
   - **d.appendleft('b') # 在最左边添加一个元素，此时 d=deque(['b', 'a'])**
   - d.extend(['c','d']) # 在最右边添加所有元素，此时 d=deque(['b', 'a', 'c', 'd'])
   - d.extendleft(['e','f']) # 在最左边添加所有元素，此时 d=deque(['f', 'e', 'b', 'a', 'c', 'd'])
   - d.pop() # 将最右边的元素取出，返回 'd'，此时 d=deque(['f', 'e', 'b', 'a', 'c'])
   - **d.popleft() # 将最左边的元素取出，返回 'f'，此时 d=deque(['e', 'b', 'a', 'c'])**
   - **d.rotate(-2) # 向左旋转两个位置（正数则向右旋转），此时 d=deque(['a', 'c', 'e', 'b'])**
   - d.count('a') # 队列中'a'的个数，返回 1
   - d.remove('c') # 从队列中将'c'删除，此时 d=deque(['a', 'e', 'b'])
   - d.reverse() # 将队列倒序，此时 d=deque(['b', 'e', 'a'])


————————————————
> 版权声明：本文为CSDN博主「HappyRocking」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
> 原文链接：https://blog.csdn.net/happyrocking/article/details/80058623

0+0
# 10-Min Stack
# 
-----------
# 题目链接
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/discuss

# 题目描述
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
 

   Hide Hint #1  
Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

# 复杂度
O(n)

# 思路
1. 最小数 还用sorted太蠢了，根本不需要将比目前最小的数大的 放进min_stack中
2. 一个规律：不用担心比目前最小的数大的那些数，因为在目前最小的这个数被pop出去之前，他们肯定先被pop出去了

5+0
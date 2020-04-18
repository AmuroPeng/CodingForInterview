# 17-Number of Islands
# 
-----------
# 题目链接
https://leetcode.com/problems/number-of-islands/

# 题目描述
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

# 复杂度
1. 时间复杂度 O(M*N)
2. 空间复杂度 O(M*N)

# 思路
1. 深度优先：递归，费时间省空间（这就是为什么有的题目可以有有剪枝，因为递归了很多没用的东西）
2. 广度优先：队列，费空间省时间（每次只需要看上下左右有没有就好了，只关注遍历到的那个数字。遍历到的就加入队列中）
3. 并查集：相同的放入dict中，直接遍历按顺序找

https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/

0+0
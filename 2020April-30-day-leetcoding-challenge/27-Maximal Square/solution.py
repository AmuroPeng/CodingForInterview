class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                    if i == 0 or j == 0:
                        res = max(matrix[i][j], res)
                    else:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])+1
                        res = max(matrix[i][j], res)
                else:
                    matrix[i][j] = 0
        return res**2


# 作者：cumt_scx
# 链接：https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-yuan-di-geng-gai-ju-zhen-sh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
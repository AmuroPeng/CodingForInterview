import math

class Solution:
    def maximalSquare(self, matrix: list) -> int:
        max_=0
        if len(matrix)==1:
            return int(matrix[0][0])
        for m in range(len(matrix)):# 最后一行一列不检查，要不然之后的就报错
            for n in range(len(matrix[0])):
                if int(matrix[m][n])==1:
                    # print(min(matrix[m+1:][n:],matrix[m:][n+1:],matrix[m+1:][n+1:]))
                    # print(type(min(matrix[m+1:][n:],matrix[m:][n+1:],matrix[m+1:][n+1:])))
                    max_=max(max_,1,1+(1+int((min(self.maximalSquare(matrix[m+1:][n:]),self.maximalSquare(matrix[m:][n+1:]),self.maximalSquare(matrix[m+1:][n+1:])))**0.5))**2)
        return max_*max_

if __name__ == "__main__":
    s=Solution()
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# -*- coding:utf-8 -*-

# 题目描述
# 给定一个数组A[0,1,...,n-1]
# 请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。


class Solution:
    def multiply(self, A):
        # write code here
        if A == []:
            return []
        else:
            B = []
            front = [1]
            behind = [1]
            num = 1
            for index, n in enumerate(A[1:]):
                num = num*A[index]
                front.append(num)
            # revlist= A[1:]
            # revlist.reverse()
            revlist = reversed(A[1:])
            num = 1
            for index, n in enumerate(revlist):
                num = num*n
                behind.append(num)
            behind.reverse()
            for index, n in enumerate(front):
                # print(behind[index])
                B.append(n*behind[index])
            return B


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply([2, 3, 4, 5]))

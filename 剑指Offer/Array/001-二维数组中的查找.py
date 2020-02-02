# -*- coding:utf-8 -*-

# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = 0
        col = len(array[0]) - 1
        while array != []:
            # print(array[row][col])
            if array[row][col] == target:
                return True
            elif target > array[row][col] and row != len(array[0]) - 1:
                row = row + 1
                continue
            elif target < array[row][col] and col != 0:
                col = col - 1
                continue
            else:
                return False
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.Find(14, [[1, 2, 8, 9], [
          2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))


# 复杂度:O(o+m)
# 思路：
# 1.数组矩阵是有序的->可以二分 
# 2.数组矩阵是有序的->可以通过比一个数，来排除某一行或者某一列->从一个位置开始做，一边比较一边排除，缩小范围 
# 3.数组矩阵是有序的+二维矩阵->复杂度应该是O(n)级别

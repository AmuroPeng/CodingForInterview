# -*- coding:utf-8 -*-

# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


class Solution:
    # s字符串

    def isNumeric(self, s, sign, point, e, begin):
        # write code here
        # （正负号）+小数   正负号+整数+E+正负号+整数
        if s == '':
            if e == 1:
                return False
            return True
        elif s[0] == '+' or s[0] == '-':
            if begin == 1 or len(s) == 1 or e == 2:
                return False
            elif e == 1:  # 可以加正负号
                e = 2  # 不能加任何符号
                return self.isNumeric(s[1:], sign, point, e, begin)
            else:
                begin = 1
                sign = 1
                return self.isNumeric(s[1:], sign, point, e, begin)
        elif s[0] == '.':
            if len(s) == 1 or point == 1 or begin == 0:
                return False
            else:
                point = 1
                return self.isNumeric(s[1:], sign, point, e, begin)
        elif s[0] == 'e' or s[0] == 'E':
            if sign == 1 or len(s) == 1 or point == 1 or e != 0 or begin == 0:
                return False
            begin = 0
            e = 1
            point = 1
            return self.isNumeric(s[1:], sign, point, e, begin)

        elif e == 1:
            e = 2
            return self.isNumeric(s[1:], sign, point, e, begin)
        else:
            begin = 1
            return self.isNumeric(s[1:], sign, point, e, begin)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isNumeric('+100', sign=0, point=0, e=0, begin=0))  # True
    print(solution.isNumeric('5e2', sign=0, point=0, e=0, begin=0))  # True
    print(solution.isNumeric('12e', sign=0, point=0, e=0, begin=0))  # False
    print(solution.isNumeric('1.2.3', sign=0, point=0, e=0, begin=0))  # False
    print(solution.isNumeric('12e+4.3', sign=0, point=0, e=0, begin=0))  # False

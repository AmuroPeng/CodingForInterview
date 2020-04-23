import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        list_ = ['0']*int(math.sqrt(100))
        # list_[-1] = '0'
        min_ = len(bin(n)[2:])
        # if min_ == 1:
        #     return 0

        # if len(bin(n)[2:]) > min_:
        #     n = pow(2, min_)-1
        for i in reversed(range(1,min_)):
            if m >= pow(2, i):
                m -= pow(2, i)
                n -= pow(2, i)
                list_[-i-1] = '1'
            elif n >= pow(2, i):
                n -= pow(2, i)
        return int(('0b'+''.join(list_)), 2)


if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(2, 4))

# import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k = 0
        while n != m:
            n >>= 1
            m >>= 1
            k += 1
        return n << k


# if __name__ == "__main__":
#     s = Solution()
#     print(s.rangeBitwiseAnd(2, 4))

class Solution:
    def numSteps(self, s: str) -> int:
        if s == '1':
            return 0
        step = 0
        # print(s)
        # print(int(s))
        # num = bin(0)
        # num = bin(int(s, 2))
        # print(type(num))
        num = bin(int(s, 2))
        # print(bin(int(num,2)))
        while num != '0b1':
            # print(s)
            # print(str(bin(int(s,2))))
            if num[-1] == '1':
                num = bin(int(num[2:], 2)+0b1)
                # num = num+0b1
            else:
                num = num >> 1
            step += 1
        return step
        # step += self.numSteps(num[2:])
        # return step
        # print(str(num))


if __name__ == "__main__":
    s = Solution()
    print(s.numSteps("1101"))

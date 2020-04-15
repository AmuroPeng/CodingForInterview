class Solution:
    def stringShift(self, s: str, shift: list) -> str:
        result = int(sum(2*(float(i)-0.5)*j for i, j in shift))%len(s)
        print(result)
        if result == 0:
            return s
        # elif result > 0:  # 右移
        return s[-result:]+s[:-result]
        # else:  # 左移
        #     result = -result
        #     return s[result:]+s[:result]


if __name__ == "__main__":
    s = Solution()
    print(s.stringShift("wpdhhcj", [[0, 7], [1, 7], [
          1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]))

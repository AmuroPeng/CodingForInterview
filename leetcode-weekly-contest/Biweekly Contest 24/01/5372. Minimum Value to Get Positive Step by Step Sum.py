class Solution:
    def minStartValue(self, nums: list) -> int:
        if nums == []:
            return 1
        min_ = 0
        count = 0
        for i in nums:
            count += i
            min_ = min(count, min_)
        return 1-min_


if __name__ == "__main__":
    s = Solution()
    print(s.minStartValue([-3, 2, -3, 4, 2]))

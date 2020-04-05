class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        count = 0
        satisfaction = sorted(satisfaction)
        max_curr = 0
        if satisfaction[-1] < 0:
            return 0
        satisfaction1=satisfaction
        for i in range(len(satisfaction)):
            if sum(satisfaction1) < 0:
                satisfaction1=satisfaction1[1:]
        for i in satisfaction1:
            count += 1
            max_curr += count*i
        return max_curr


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSatisfaction([-1, -8, 0, 5, -9]))

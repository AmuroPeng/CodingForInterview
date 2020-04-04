class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if s == '':
            return True
        if len(s) < k:
            return False
        dic = {}
        count = 0
        for i in str(s):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for key, value in dic.items():
            if float(value)/2-int(int(value)/2) != 0.0:  # 奇数
                count += 1
        if count <= k:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    print(solution.canConstruct('leetcode', 2))

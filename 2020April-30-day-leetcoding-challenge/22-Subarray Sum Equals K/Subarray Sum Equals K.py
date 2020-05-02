class Solution:
    def subarraySum(self, nums: list, k: int) -> int:

        dict_ = {0: 1}
        # if k == 0:
        #     dict_[0] = 0
        count = 0
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_-k in dict_:
                count += dict_[sum_-k]
            if sum_ in dict_:
                dict_[sum_] += 1
            else:
                dict_[sum_] = 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1], 0))

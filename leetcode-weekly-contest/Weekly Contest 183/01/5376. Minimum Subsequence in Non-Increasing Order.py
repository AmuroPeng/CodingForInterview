class Solution:
    def minSubsequence(self, nums: list) -> list:
        p_right = len(nums)-1
        nums = sorted(nums)
        if nums == []:
            return []
        if len(nums) == 1:
            return nums
        count_left = 0
        count_right = nums[-1]
        for p_left in range(len(nums)):
            if p_left == p_right:
                break
            count_left += nums[p_left]
            if count_left >= count_right:
                p_right -= 1                                   
                count_right += nums[p_right]
            if p_left == p_right:
                break
        return sorted(nums[p_right:], reverse=True)


if __name__ == "__main__":
    s = Solution()
    print(s.minSubsequence([8,8]))

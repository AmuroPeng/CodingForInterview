class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p_curr = 0
        if nums == []:
            return nums
        for p in range(len(nums)):
            if nums[p] != 0:
                nums[p_curr], nums[p] = nums[p], nums[p_curr]
                p_curr += 1
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))

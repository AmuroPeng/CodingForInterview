class Solution:
    def maxProduct(self, nums: list) -> int:
        # if len(nums) == 2:
        #     return (nums[0]-1)*(nums[1]-1)
        nums = sorted(nums, reverse=True)
        return (nums[0]-1)*(nums[1]-1)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([3, 4, 5, 2]))

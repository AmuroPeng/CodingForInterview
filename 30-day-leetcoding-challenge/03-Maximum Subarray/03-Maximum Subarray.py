class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        # min_sum = nums[0]
        count = 0
        for i in nums:
            count += i
            if count < 0:
                max_sum = max(max_sum, i)
                count = 0
            elif count > max_sum:
                max_sum = count
        return max_sum

        # 大佬解法看着帅气
        # maxcurr = nums[0]
        # maxglobal = nums[0]
        # for i in range(1,len(nums)):
        #     maxcurr = max(nums[i], maxcurr + nums[i]) 
        # 这两个数相比，就和0，curr相比一样，所以本质没有区别
        #     maxglobal = max(maxcurr, maxglobal)
        # return maxglobal
    

if __name__ == "__main__":
    solution = Solution()
    # print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

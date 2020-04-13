class Solution:
    def findMaxLength(self, nums: list) -> int:

        def counting(nums):

            # 2.把两头多的去掉，看看够不够相等
            while nums[0] == 0 and self.count > 0:
                nums = nums[1:]
                self.count -= 1
            while nums[-1] == 0 and self.count > 0:
                nums = nums[:-2]
                self.count -= 1
            if self.count == 0:
                return len(nums)
                # 3.如果还是多，那就中间劈开，看少的数，左边多还是右边多，选多的那边
            else:
                # 大于右边多，小于左边多
                if sum(i for i in nums[len(nums)//2:]) > sum(i for i in nums[:len(nums)//2]):
                    nums = nums[1:]
                    self.count += 1
                else:
                    nums = nums[:-1]
                    self.count += 1
                if self.count == 0:
                    return len(nums)
                else:
                    counting(nums)

        # 1.看0多还是1多
        self.count = len(nums)-2 * sum(i for i in nums)  # 正数0多，负数1多
        # self.count = 1
        if self.count == 0:
            return len(nums)
        elif len(nums) == nums.count(0)or len(nums) == nums.count(1):
            return 0
        elif self.count < 0:
            nums = [1-i for i in nums]  # 都变成0多1少
        return counting(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxLength([0,1,1,0,1,1,1,0]))

class Solution:
    def findMaxLength(self, nums: list) -> int:
        # 用多动态规划 没做出来
        def counting(nums, count):

            # 2.把两头多的去掉，看看够不够相等
            while nums[0] == 0 and count > 0:
                nums = nums[1:]
                count -= 1
            while nums[-1] == 0 and count > 0:
                nums = nums[:-1]
                count -= 1
            if count == 0:
                # print(len(nums))
                return len(nums)
                # 3.如果还是多，那就中间劈开，看少的数，左边多还是右边多，选多的那边
            else:
                # 大于右边多，小于左边多
                if sum(i for i in nums[len(nums)//2:]) > sum(i for i in nums[:len(nums)//2]):
                    nums = nums[1:]
                    count += 1
                else:
                    nums = nums[:-1]
                    count += 1
                if count == 0:
                    print(len(nums))
                    return len(nums)
                else:
                    return counting(nums, count)

        # 1.看0多还是1多
        count = len(nums)-2 * sum(i for i in nums)  # 正数0多，负数1多
        # self.it = len(nums)-2 * sum(i for i in nums)
        if count == 0:
            return len(nums)
        elif len(nums) == nums.count(0)or len(nums) == nums.count(1):
            return 0
        elif count < 0:
            nums = [1-i for i in nums]  # 都变成0多1少
            count = -count
        return counting(nums, count)


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))

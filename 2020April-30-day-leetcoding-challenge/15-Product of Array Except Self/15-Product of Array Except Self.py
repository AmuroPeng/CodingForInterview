class Solution:
    def productExceptSelf(self, nums: list) -> list:
        if len(nums) < 2:
            return nums
        left = [1]
        right = [1]
        # for i in range(1, len(nums)):
        for i in nums:
            # left = [left[i]*nums[j] for j in left[:i]] + \
                # [left[i]]+[left[i]*nums[j] for j in left[i:]]
            left.append(left[-1]*i)
        left.pop()
        reverse_ = nums
        reverse_.reverse()
        for i in reverse_:
            right.append(right[-1]*i)
        right.reverse()
        right =right[1:]
        return [left[i]*right[i] for i in range(0,len(nums))]
            

        # return left


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))

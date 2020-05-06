class Solution:
    def majorityElement(self, nums: list) -> int:
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
            if dict_[i] > len(nums)/2:
                return i


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))

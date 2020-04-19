class Solution:
    def search(self, nums: list, target: int) -> int:
        if nums == []:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        low = 0
        high = len(nums)-1
        mid = high//2
        while low < high:
            if nums[mid] == target:
                return mid
            if nums[high] == target:
                return high
            if nums[low] == target:
                return low
            if nums[low] <= nums[mid-1]:  # in order
                if target > nums[low] and target <= nums[mid-1]:
                    high = mid-1
                    mid = (low+high)//2
                else:
                    low = mid+1
                    mid = (low+high)//2
            else:
                if target >= nums[mid+1] and target < nums[high]:
                    low = mid+1
                    mid = (low+high)//2
                else:
                    high = mid-1
                    mid = (low+high)//2

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search(nums=[2,3,4,5,6,7,8,9,1], target=9))

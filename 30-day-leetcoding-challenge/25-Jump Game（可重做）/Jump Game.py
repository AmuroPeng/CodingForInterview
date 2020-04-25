class Solution:
    def canJump(self, nums: list) -> bool:
        if nums == []:
                return True
        list_ = [len(nums)-1,len(nums)]
        for i in reversed(range(len(nums))):
            
            print(f"i {i}   ,nums[i] {nums[i]}  ,list_: {list_}")
            # f"i"+str(i)+"   nums[i]"+str(nums[i])

            if i + nums[i] in list_:
                if i==0:
                    return True
                print(1)
                # self.canJump(nums[:-i-1])
                list_.append(i)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([3,2,1,0,4]))

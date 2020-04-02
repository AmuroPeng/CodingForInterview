# -*- coding:utf-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1
        # for i in nums:
        #     if nums.count(i)== 1:
        #         return i
        # return None

        # 方法2
        dic={}
        for i in nums:
            if i in dic:
                del dic[i]
            else:
                dic[i]=0
            # print(dic)
        for i in dic.keys():
            return i
        # a = dic.keys()
        # print list(a)
        # return dic.keys()[0]
        
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([2,2,1]))    
    print(solution.singleNumber([4,1,2,1,2]))
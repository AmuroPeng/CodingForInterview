class Solution:
    # def isHappy(self, n: int) -> bool:
        # try:
        #     if n == 1:
        #         return True
        #     else:
        #         num = 0
        #         for i in str(n):
        #             num += pow(int(i),2)
        #         return self.isHappy(num)
        # except:
        #     return False
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        res = sum([int(x)**2 for x in str(n)])
        result_table = []
        while res != 1:
            res = sum([int(x)**2 for x in str(res)])
            if res in result_table:
                return False
            else:
                result_table.append(res)
                
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))
    print(solution.isHappy(111))
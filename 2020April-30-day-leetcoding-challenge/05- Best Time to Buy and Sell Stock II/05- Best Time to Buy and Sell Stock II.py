class Solution:
    def maxProfit(self, prices: list) -> int:
        if prices == []:
            return 0
        count_all = 0
        p_curr = 0
        for p in range(1, len(prices)):
            if prices[p] < prices[p-1]:
                count_all += prices[p-1]-prices[p_curr]
                print(str(prices[p-1])+'-' +
                      str(prices[p_curr])+',count='+str(count_all))
                p_curr = p
            elif p == len(prices)-1:
                count_all += prices[p]-prices[p_curr]
        return count_all


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1,2,3,4,5]))

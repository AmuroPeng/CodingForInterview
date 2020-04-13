class Solution:
    def lastStoneWeight(self, stones: list) -> list:
        if stones == []:
            return 0
        def weight(stones):
            if len(stones) == 1:
                return stones[0]
            elif len(stones) == 2:
                return abs(stones[0]-stones[1])
            else:
                stones = sorted(stones, reverse=1)
                if stones[0]==stones[1]:
                    return weight(stones[2:])
                return weight([stones[0]-stones[1]]+stones[2:])
        return weight(stones)

# 大佬做法
    #     class Solution:
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     h = [-x for x in stones]
    #     heapq.heapify(h)
    #     while(len(h)>1 and h[0] != 0):
    #         diff = heapq.heappop(h) - heapq.heappop(h)
    #         heapq.heappush(h,diff)
    #     return -h[0]


if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))

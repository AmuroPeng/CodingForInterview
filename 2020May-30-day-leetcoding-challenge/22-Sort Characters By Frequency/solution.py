class Solution:
    def frequencySort(self, s: str) -> str:
        # 大顶堆
        countFrequency = collections.defaultdict(int)
        for i in s:
            countFrequency[i] += 1
        lst = []
        heapq.heapify(lst)
        for i in countFrequency:
            for j in range(countFrequency[i]):
                heapq.heappush(lst, (-countFrequency[i], i))
        
        return ''.join([heapq.heappop(lst)[1] for _ in range(len(s))])

# 作者：cui-jin-hao-_official
# 链接：https://leetcode-cn.com/problems/sort-characters-by-frequency/solution/python-counterda-ding-dui-tong-pai-xu-by-cui-jin-h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
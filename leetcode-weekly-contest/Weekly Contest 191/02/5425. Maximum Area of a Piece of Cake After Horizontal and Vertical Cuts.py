class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        max_h = 0
        for i in range(len(horizontalCuts)-1):
            max_h = max(max_h, horizontalCuts[i+1]-horizontalCuts[i])
        max_v = 0
        for i in range(len(verticalCuts)-1):
            max_v = max(max_v, verticalCuts[i+1]-verticalCuts[i])
        return max_h*max_v

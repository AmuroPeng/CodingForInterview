class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: return '0'
        
        stack = []
        
        for n in num:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # 现在栈里是递增数列，k还没用完，当然是从大的开始删了
        for _ in range(k):
            stack.pop()
        
        ans = ''.join(stack).lstrip('0')
        # ans可能被strip空了
        return ans or '0'

# 作者：deerhound
# 链接：https://leetcode-cn.com/problems/remove-k-digits/solution/jian-ji-de-dan-diao-zhan-shi-xian-by-deerhound/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=0,n
        while l<r:
            m=(l+r)//2
            if isBadVersion(m):
                r=m
            else:
                l=m+1
        return l

# 作者：jutraman
# 链接：https://leetcode-cn.com/problems/first-bad-version/solution/pythondi-yi-ge-cuo-wu-de-ban-ben-by-jutraman/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
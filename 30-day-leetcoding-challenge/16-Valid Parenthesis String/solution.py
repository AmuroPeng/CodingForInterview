class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop(0)
                else:
                    return False
        
        while left and star:
            if left[0] > star[0]:
                star.pop(0)
            else:
                star.pop(0)
                left.pop(0)
        
        if left:
            return False
        return True
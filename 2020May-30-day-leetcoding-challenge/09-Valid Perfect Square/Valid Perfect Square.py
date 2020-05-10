class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 2
        while num != 1:
            if num<pow(s,2):
                return False
            if num%(pow(s,2)):
                s+=1
            else:
                num = num/(pow(s,2))
                s=2
        return True
            
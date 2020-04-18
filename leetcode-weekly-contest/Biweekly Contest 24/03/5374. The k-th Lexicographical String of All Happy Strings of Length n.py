class Solution:
    def getHappyString(self, n: int, k: int, p='', last_char=0) -> str:
        if len(p) == n:
            print(len(p))
            k -= 1
        else:
            for i in ['a', 'b', 'c']:
                if last_char != i:
                    k,p = self.getHappyString(n, k, p+i, i)
                    print(str(p+i)+'   '+str(k)+'    '+str(len(p)))
                if k == 0:
                    return p+i
        return k,p


if __name__ == "__main__":
    s = Solution()
    print(s.getHappyString(3, 9))

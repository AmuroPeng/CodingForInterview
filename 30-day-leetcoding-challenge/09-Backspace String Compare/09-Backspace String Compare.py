class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = []
        for i in S:
            if i == "#" :
                if a != []:
                    a.pop()
            else:
                a.append(i)
            print(a)
        b = []
        for i in T:
            if i == "#" :
                if b != []:
                    b.pop()
            else:
                b.append(i)
            print(b)
        return a == b


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("y#fo##f", "y#f#o##f"))


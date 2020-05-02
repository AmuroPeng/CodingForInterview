import collections


class Solution:
    def checkValidString(self, s: str) -> bool:
        # chars = collections.deque(s)
        # left = 0
        # right = 0
        chars = []
        count = 0
        for i in s:
            if i == "(" or i == "*":
                chars.append(i)
            else:  # ")"
                if chars == []:
                    if count:
                        count -= 1
                    else:
                        return False
                elif chars[-1] == "(":
                    chars.pop()
                else:
                    for j in reversed(chars):
                        if j == "*":
                            chars.pop()
                            count += 1
                        else:
                            chars.pop()
                            break
        while chars:
            if chars[-1] == "*":
                count += 1
                chars.pop()
            else:  # "("
                if count:
                    count -= 1
                    chars.pop()
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.checkValidString("(*))"))

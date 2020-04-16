import collections


class Solution:
    def checkValidString(self, s: str) -> bool:
        # chars = collections.deque(s)
        # left = 0
        # right = 0
        chars=[]
        while chars :
            if chars[0] == "*":
                chars.popleft()
                left += 1
            elif chars[0] == "(":
                if chars[-1] == "*":
                    right += 1
                    chars.pop()
                elif chars[-1] == ")":
                    chars.popleft()
                    chars.pop()
                else:  # ")"
                    if right:
                        chars.popleft()
                        right -= 1
                    else:
                        return False
            else:  # ")"
                if left:
                    chars.pop()
                    left -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.checkValidString("(*))"))

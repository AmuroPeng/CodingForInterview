class Solution:
    def minTime(self, n: int, edges: list, hasApple: list) -> int:
        count = 0  # 记录0作为i[0]的次数，判断是不是需要经过0
        dict_ = {0: 1}
        set_ = set()
        for i in reversed(edges):
            print(f"i", i)
            if i[1] in set_ and i[0] in set_:
                pass
            elif i[1] in set_:
                set_.add(i[0])
            else:
                if hasApple[i[1]]:
                    set_.add(i[1])
                    set_.add(i[0])
                if hasApple[i[0]] and i[0] not in set_:
                    set_.add(i[0])
            if i[0] == 0 and i[1] in set_:
                count = 2
            print(f"set_", set_, "\n")
        return len(set_)*2-count


if __name__ == "__main__":
    s = Solution()
    print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [
        False, False, True,  False, True, True, False]))

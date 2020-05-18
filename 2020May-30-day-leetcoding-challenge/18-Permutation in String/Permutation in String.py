class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_ = {}
        for i in s1:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        # print(dict_)
        left = 0
        right = 0
        while(right < len(s2)):
            if s2[right] in dict_:
                dict_[s2[right]] -= 1
            if (right-left > len(s1)-1):
                if s2[left] in dict_:
                    dict_[s2[left]] += 1
                left += 1
            # print(f"\nleft",left,s2[left],"\tright",right,s2[right])
            right += 1
            flag = 0
            for k, v in dict_.items():
                if v != 0:
                    flag = 1
            if flag == 0:
                return True
            # print(f"dict_: ",dict_)
        return False


if __name__ == "__main__":
    # pass
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))

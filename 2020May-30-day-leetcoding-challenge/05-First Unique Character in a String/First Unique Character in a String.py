import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_ = collections.OrderedDict()
        for i in range(len(s)):
            if s[i] not in dict_:
                dict_[s[i]] = [i]
            else:
                dict_[s[i]].append(i)
        for key, value in dict_.items():
            if len(value) == 1:
                return value[0]
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("loveleetcode"))

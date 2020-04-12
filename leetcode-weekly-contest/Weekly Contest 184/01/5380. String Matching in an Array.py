class Solution:
    def stringMatching(self, words: list) -> list:
        words = sorted(words, key=lambda i: len(i))
        list_ = []
        for pattern in range(len(words)):  # 每个匹配字符串
            sign = 0
            for word in range(pattern+1, len(words)):  # 每个要被匹配的字符串
                for character in range(len(words[word])):  # 每个匹配时的指针
                    if words[pattern] == words[word][character:character+len(words[pattern])]:
                        sign = 1
                        break
                if sign == 1:
                    list_.append(words[pattern])
                    break
        return list_


if __name__ == "__main__":
    s = Solution()
    print(s.stringMatching(["mass", "as", "hero", "superhero"]))

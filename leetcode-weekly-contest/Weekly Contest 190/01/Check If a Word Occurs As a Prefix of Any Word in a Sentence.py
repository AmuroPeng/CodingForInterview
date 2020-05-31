class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if searchWord == '' or sentence == '':
            return -1
        list_ = sentence.split()
        for i in range(len(list_)):
            if len(searchWord) <= len(list_[i]) and searchWord == list_[i][:len(searchWord)]:
                return i+1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.isPrefixOfWord(sentence="i love eating burger", searchWord="burg"))

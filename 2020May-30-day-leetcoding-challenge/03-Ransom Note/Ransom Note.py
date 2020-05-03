class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == "":
            return True
        list_=list(magazine)
        for i in ransomNote:
            if i in list_:
                list_.remove(i)
            else:
                return False
        return True
        

if __name__ == "__main__":
    s=Solution()
    print(s.canConstruct("aa", "aab"))
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        left = right = 0
        count = 0
        max_ = 0
        while right != len(s):
            if s[right] in vowel:
                count += 1


            if right-left == k:
                if s[left] in vowel:
                    count -= 1
                left += 1
            right += 1
            max_ = max(max_, count)

        return max_


if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels(s="abciiidef", k=3))

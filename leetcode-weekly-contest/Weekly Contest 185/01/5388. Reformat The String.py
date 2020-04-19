class Solution:
    def reformat(self, s: str) -> str:
        digit = []
        alpha = []
        for i in s:
            if i.isdigit():
                digit.append(i)
            elif i.isalpha():
                alpha.append(i)
        # print(digit)
        # print(alpha)
        if len(s)==1:
            return s
        if len(digit)-len(alpha) == 1:
            result = ""
            for i in range(len(alpha)):
                result += (str(digit[i]))
                result += (str(alpha[i]))
            result += (digit[i+1])
            return result
        elif len(digit)-len(alpha) == -1:
            result = ""
            for i in range(len(digit)):
                # print(i)
                # print(len(alpha))
                result += (str(alpha[i]))
                # print(result)
                result += (str(digit[i]))

            result += str(alpha[i+1])
            return result
        elif len(digit)-len(alpha) == 0:
            result = ""
            for i in range(len(alpha)):
                result += (str(alpha[i]))
                result += (str(digit[i]))
            return result
        return ""


if __name__ == "__main__":
    s = Solution()
    print(s.reformat("j"))

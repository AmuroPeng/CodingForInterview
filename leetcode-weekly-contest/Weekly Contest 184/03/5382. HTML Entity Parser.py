class Solution:
    def entityParser(self, text: str) -> str:
        dict_ = {"&quot;": '"', "&apos;": "'", "&amp;": "&",
                 "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        str_ = ""
        i = 0
        while i < len(text):
            if text[i] == "&":
                if text[i:i+3]in dict_:
                    str_ = str_ + dict_[text[i:i+3]]
                    i = i+3
                elif text[i:i+4]in dict_:
                    str_ = str_ + dict_[text[i:i+4]]
                    i = i+4
                elif text[i:i+5]in dict_:
                    str_ = str_ + dict_[text[i:i+5]]
                    i = i+5
                elif text[i:i+6]in dict_:
                    str_ = str_ + dict_[text[i:i+6]]
                    i = i+6
                elif text[i:i+7]in dict_:
                    str_ = str_ + dict_[text[i:i+7]]
                    i = i+7
                else:
                    str_ = str_+text[i]
                    i += 1
            else:
                str_ = str_+text[i]
                i += 1
        return str_


if __name__ == "__main__":
    s = Solution()
    # print(s.entityParser("&amp;.dd"))
    print(s.entityParser('"&quot;...&quot;"'))

import collections


class Solution:
    def arrangeWords(self, text: str) -> str:
        dict_ = dict()
        word = ''
        p = 0
        q = 0
        text = text.lower()

        while q != len(text)+1:
            if q == len(text):
                if q-p not in dict_:
                    dict_[q-p] = [text[p:]]
                else:
                    dict_[q-p].append(text[p:])
                break
            if text[q] == ' ':
                print(text[p:q])
                print(p,text[p],q,text[q])
                if q-p not in dict_:
                    dict_[q-p] = [text[p:q]]
                else:
                    dict_[q-p].append(text[p:q])
                q += 1
                p = q
            else:
                q += 1

        str_ = ''
        for k, v in collections.OrderedDict(sorted(dict_.items(), key=lambda t: t[0])).items():
            for i in v:
                str_ += i
                str_ += ' '
        str_ = str_[0].upper()+str_[1:-1]

        return str_

if __name__ == "__main__":
    s=Solution()
    print(s.arrangeWords("Leetcode is cool"))
# -*- coding:utf-8 -*-

# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
# 如果当前字符流没有存在出现一次的字符，返回#字符


class Solution:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.result = []

    def FirstAppearingOnce(self):
        # write code here
        for n in self.result:
            if n != '#':
                return n
        return '#'

    def Insert(self, char):
        # write code here
        if char in self.dic:
            self.result[self.dic[char]] = '#'
        else:
            self.result.append(char)
            self.dic[char] = len(self.result)-1
        return self.FirstAppearingOnce()


if __name__ == "__main__":
    solution = Solution()
    while 1:
        input_char = input('输入一个字符：')
        print(solution.Insert(input_char[0]))

# 1.
# 在Insert中，list(string)遍历,用dict存位置
# 在FirstAppearingOnce中：遇见hasKey的话，value指的list对应的value置为'#'
# 全部搞完，从头遍历。第一个不是#的元素就是答案
# 2.
# 看完答案，时间复杂度基本都是O(n)或者带遍历的伪O(1)，感觉可以改进到O(1)，发现重复后dict的value置为#，但list不需要置为#，直接删掉就好，保证每次list[0]都是当前要的答案。
# （把list当队列用，但是不需要在发现重复的时候进行队列的遍历）
# ↑太蠢了，remove之后list的index就变了，没法用了gg

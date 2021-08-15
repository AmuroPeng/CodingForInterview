# -*- coding:utf-8 -*-

# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
# 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here

        list_pattern = list(pattern)
        list_s = list(s)
        index_s = 0
        # 先写了一遍遍历s的，发现分类讨论过于复杂：无法讨论.和*时的所有情况
        for index_pattern in range(len(list_pattern)):
            if index_s = len(list_s)-1:  # 到达s最后一位
                return False
            # 匹配上了➡️继续
            elif list_s[index_s] == list_pattern[index_pattern]:
                index_s += 1
            # 没有匹配上➡️
            # 出现*➡️忽略
            elif list_pattern[index_pattern] == '*':
                continue
            # 出现除A*.外的字符➡️看后面一位是不是*：如果是，加dic并忽略；如果不是则False
            elif list_pattern[index_pattern] != '*' or '.' or s[index_s]
               if index_pattern == len(pattern)-1:  # 最后一位不匹配
                    return False
                elif list_pattern[index_pattern+1] ==
            # 出现.是重点➡️如果字符串中还有*，则可以忽略也可以算作是匹配上了；如果字符串中没有*，则把.当作匹配字符来进行判断
            elif  list_pattern[index_pattern] == '.':
                
        if index_s == len(s)-1:
            也到达s最后一位
            return True
        else:  # 未到达s最后一位
            return False
        #


if __name__ == "__main__":
    solution = Solution()
    print(solution.match('aaa', "a.b*c*a"))  # True
    # print(solution.match('aaa', "ab*ac*a"))  # True
    # print(solution.match('aaa', "a.ab*c*a"))  # True
    # print(solution.match('aaa', "ab*c*a"))  # False
    # print(solution.match('aaa', "aa.a"))  # False
    # print(solution.match('aaa', "ab*a"))  # False

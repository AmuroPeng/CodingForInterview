class Solution:
    def groupAnagrams(self, strs: list) -> list:
        if strs == []:
            return []
        result = {}
        count_blank = 0
        for i in strs:
            # if i == '':
            #     count_blank += 1
            if str(sorted(i)) not in result:
                result[str(sorted(i))] = [i]
            else:
                result[str(sorted(i))].append(i)
        result_list=[]
        # if count_blank != 0:
        #     for i in range(count_blank)
        #     result_list.append([''])
        for i,v in result.items():
            result_list.append(v)
        return result_list

        # 大佬简洁版
        # ans = collections.defaultdict(list)
        # for i in strs:
        #     ans[tuple(sorted(i))].append(i)
        # return ans.values()


if __name__ == "__main__":
    s = Solution()
    print(sorted('abcdkfl'))
    # print(set('acbkdlf'))
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

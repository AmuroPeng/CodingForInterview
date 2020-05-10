class Solution:
    def findJudge(self, N: int, trust: list) -> int:
        if trust == []:
            return 1
        dict_ = {}
        set_=set([x+1 for x in range(N)])
        list_=[]
        for i in trust:
            if i[1] not in dict_:
                dict_[i[1]] = 1
            else:
                dict_[i[1]] += 1
            if i[0] in set_:
                set_.remove(i[0])
        # print(dict_)
        # print(set_)
        for key in set_:
            if key in dict_ and dict_[key]==N-1:
                list_.append(key)
        # print(list_)
        if len(list_)==1:
            return list_[0]
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
# 不能在i[0],存在n-1遍i[1]
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        check = []
        list_len = 0
        for i in range(1,n+1):
            count = 0
            for j in str(i):
                count += int(j)

            if i not in check:
                check.append(i)
                if count not in dic:
                    dic[count] = [i]
                    list_len = max(1,list_len)
                else:
                    dic[count].append(i)
                    list_len = max(list_len, len(dic[count]))
                    print(list_len)

        result = 0
        for key, value in dic.items():
            if len(value) == list_len:
                result += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.countLargestGroup(101))

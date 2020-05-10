class Solution:
    def buildArray(self, target: list, n: int) -> list:
        list_ = []
        p = 1
        for i in range(len(target)):
            while(p != target[i]):
                list_.append("Push")
                list_.append("Pop")
                print(list_)
                p += 1
            list_.append("Push")
            print(list_)
            if p == target[-1]:
                print("final")
                print(list_)
                return list_
            else:
                p += 1


if __name__ == "__main__":
    s = Solution()
    print(s.buildArray([1, 3], 3))

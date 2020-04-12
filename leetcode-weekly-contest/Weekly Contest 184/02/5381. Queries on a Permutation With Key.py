class Solution:
    def processQueries(self, queries: list, m: int) -> list:
        P = list(i+1 for i in range(m))
        list_ = []

        for i in queries:
            move = P.index(i)
            list_.append(move)
            P = [P[move]]+P[:move]+P[move+1:]
        return list_


if __name__ == "__main__":
    s = Solution()
    print(s.processQueries(queries=[3, 1, 2, 1], m=5))

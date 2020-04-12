class Solution:
    def processQueries(self, queries: list, m: int) -> list:
        P = []
        list_=[]
        for i in range(m):
            P.append(i+1)

        for i in queries:
            move = P.index(i)
            list_.append(move)
            left = P[:move]
            # if move == 0:
            #     left =[]
            right = P[move+1:]
            # if move == len(P):
            #     right =[]
            P = [P[move]]+list(left)+list(right)
            # print(P)
        return list_

if __name__ == "__main__":
    s = Solution()
    print(s.processQueries(queries=[3, 1, 2, 1], m=5))

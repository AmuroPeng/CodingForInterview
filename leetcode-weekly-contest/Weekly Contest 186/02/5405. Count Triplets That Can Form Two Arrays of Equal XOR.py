class Solution:
    def countTriplets(self, arr: list) -> int:
        count = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                tmp = 0
                for x in range(i, j+1):
                    tmp ^= arr[x]
                    # print("tmp"+str(tmp))
                if tmp == 0:
                    print(i,j)
                    print("gg")
                    count += j-i
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countTriplets([2, 3, 1, 6, 7]))

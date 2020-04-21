# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """


class BinaryMatrix(object):
    def __init__(self):
        super().__init__()
        self.matrix = [[0, 0], [1, 1]]

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self) -> list:
        return [2, 2]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        self.n, self.m = binaryMatrix.dimensions()
        i = 0
        low = 0
        high = self.n-1
        return self.search(low, high, binaryMatrix, i)

    def search(self, low, high, binaryMatrix, i):

        if high < 1 or high >= self.n:
            if binaryMatrix.get(0, i) == 1:
                return 0
            elif binaryMatrix.get(self.n-1, i) == 1:
                return self.n-1
            else:
                return -1
        if i == self.m:
            return -1

        mid = (low+high)//2
        if i < self.m-1:
            if binaryMatrix.get(mid, i) == 1:
                return self.search(low, mid-1, binaryMatrix, i)
            else:
                return self.search(low, high, binaryMatrix, i+1)
        else:
            return self.search(mid+1, high, binaryMatrix, 0)


if __name__ == "__main__":
    s = Solution()
    m = BinaryMatrix()
    print(s.leftMostColumnWithOne(m))

class Solution:
    def numIslands(self, grid: list) -> int:
        self.checked = {}
        self.count = 0
        self.isCheck = []
        for i in range(len(grid)):
            # print(i)
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                else:
                    self.getCount(grid, i, j)
        return self.count

    def getCount(self, grid: list, i, j):
        self.isCheck.append(str([i, j]))
        if i-1 >= 0 and grid[i-1][j] == '1' and str([i-1, j]) in self.isCheck:
            if str([i-1, j]) in self.checked:
                self.checked[str([i, j])] = self.checked[str([i-1, j])]
            else:
                self.checked[str([i, j])] = self.getCount(grid, i-1, j)
        elif j-1 >= 0 and grid[i][j-1] == '1'and str([i-1, j]) in self.isCheck:
            if str([i, j-1]) in self.checked:
                self.checked[str([i, j])] = self.checked[str([i, j-1])]
            else:
                self.checked[str([i, j])] = self.getCount(grid, i, j-1)
        elif i+1 < len(grid) and grid[i+1][j] == '1'and str([i-1, j]) in self.isCheck:
            if str([i+1, j]) in self.checked:
                self.checked[str([i, j])] = self.checked[str([i+1, j])]
            else:
                self.checked[str([i, j])] = self.getCount(grid, i+1, j)
        elif j+1 < len(grid[0]) and grid[i][j+1] == '1'and str([i-1, j]) in self.isCheck:
            if str([i, j+1]) in self.checked:
                self.checked[str([i, j])] = self.checked[str([i, j+1])]
            else:
                self.checked[str([i, j])] = self.getCount(grid, i, j+1)
        else:
            self.count += 1
            self.checked[str([i, j])] = self.count


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))

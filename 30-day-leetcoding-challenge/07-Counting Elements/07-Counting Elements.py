class Solution:
    def countElements(self, arr: list):
        arr_set = set()
        for i in arr:
            arr_set.add(i)
        count = 0
        for i in arr:
            if i+1 in arr_set:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countElements([1, 2, 3]))

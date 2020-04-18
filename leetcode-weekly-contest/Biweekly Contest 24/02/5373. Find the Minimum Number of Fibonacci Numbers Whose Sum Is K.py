class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = self.Fibonacci(k)
        count = 0
        for i in reversed(fibonacci):
            if k == i:
                return count+1
            elif k > i:
                k -= i
                count += 1
            else:  # k<i
                continue

    def Fibonacci(self, k):
        count1 = 1
        count2 = 1
        count = [1, 1]
        sign = 1
        while count[-1] <= k:
            tmp = count1
            count1 += count2
            count.append(count1)
            count2 = tmp
        return count[:-1]

# 贪心算法

if __name__ == "__main__":
    s = Solution()
    # print(s.Fibonacci(19))
    print(s.findMinFibonacciNumbers(5))

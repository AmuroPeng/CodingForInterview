import collections


class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        queue = collections.deque()
        queue.append((sr, sc))
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        if oldColor == newColor:
            return image
        while (queue):
            m, n = queue.popleft()
            # print(f"print m,n ", m, n)
            if m > 0 and image[m-1][n] == oldColor:
                image[m-1][n] = newColor
                queue.append((m-1, n))
            if n > 0 and image[m][n-1] == oldColor:
                image[m][n-1] = newColor
                queue.append((m, n-1))
            if m < len(image)-1 and image[m+1][n] == oldColor:
                image[m+1][n] = newColor
                queue.append((m+1, n))
            if n < len(image[0])-1 and image[m][n+1] == oldColor:
                image[m][n+1] = newColor
                queue.append((m, n+1))
            # print(f"print queue: ", queue)
            # print(f"print image: ", image, "\n")
        return image


if __name__ == "__main__":
    s = Solution()
    print(s.floodFill(image=[[1, 1, 1], [1, 1, 0],
                             [1, 0, 1]], sr=1, sc=1, newColor=2))

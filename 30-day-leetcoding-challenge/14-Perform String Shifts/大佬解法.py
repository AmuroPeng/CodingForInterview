class Solution:
    def stringRotation(self, s: str, rotation: List[List[int]]) -> str:
        chars = collections.deque(s)
        for d, amount in rotation:
            if d == 0:
                for _ in range(amount):
                    num = chars.popleft()
                    chars.append(num)
            else:
                for _ in range(amount):
                    num = chars.pop()
                    chars.appendleft(num)
        return ''.join(chars)
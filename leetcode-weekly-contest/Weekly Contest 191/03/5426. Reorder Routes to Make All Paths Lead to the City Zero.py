import collections

class Solution:
    def minReorder(self, n: int, connections: list) -> int:
        dict_=collections.defaultdict(list)
        que = collections.deque(connections)
        set_ = {0}
        count = 0
        while que:
            if que[0][0] == 0:
                count += 1
                set_.add(que[0][1])
                que.popleft()
            elif que[0][1] == 0:
                set_.add(que[0][0])
                que.popleft()
            else:
                if que[0][0] in set_ and que[0][1] in set_:
                    que.popleft()
                elif que[0][0] in set_ and que[0][1] not in set_:
                    count += 1
                    set_.add(que[0][1])
                    que.popleft()
                elif que[0][0] not in set_ and que[0][1] in set_:
                    set_.add(que[0][0])
                    que.popleft()
                else:
                    tmp = que.popleft()
                    que.append(tmp)
        return count


if __name__ == "__main__":
    s=Solution()
    print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
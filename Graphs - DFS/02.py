from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False for x in isConnected]
        n = 0
        for province in range(len(isConnected)):
            queue = deque()
            if not visited[province]:
                queue.append(province)
                visited[province] = True
                n += 1
            while queue:
                q = queue.popleft()
                for i in range(len(isConnected[q])):
                    if isConnected[q][i] == 1 and not visited[i]:
                        visited[i] = True
                        queue.append(i)
        return n


print(
    Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]])
)

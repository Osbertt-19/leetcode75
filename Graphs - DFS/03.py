from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ret = 0
        visited = [False] * n
        visited[0] = True
        remaining = []
        while connections or remaining:
            first, second = connections.pop()
            if visited[first]:
                ret += 1
                visited[second] = True

            elif visited[second]:
                visited[first] = True
            else:
                remaining.append([first, second])
            if not connections:
                connections = remaining
                remaining = []
        return ret


print(Solution().minReorder(3, [[1, 2], [2, 0]]))

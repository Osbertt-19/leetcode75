from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for x in rooms]
        visited[0] = True
        keys = rooms[0]
        while keys:
            key = keys.pop(0)
            if not visited[key]:
                keys += rooms[key]
                visited[key] = True
        return all(visited)


print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

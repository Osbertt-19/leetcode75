from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        count = 0
        queue = [entrance]
        maze[entrance[0]][entrance[1]] = "+"
        while queue:
            temp = []
            for i, j in queue:
                if (
                    i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1
                ) and (i != entrance[0] or j != entrance[1]):
                    return count
                if i < len(maze) - 1 and maze[i + 1][j] == ".":
                    temp.append([i + 1, j])
                    maze[i + 1][j] = "+"
                if i > 0 and maze[i - 1][j] == ".":
                    temp.append([i - 1, j])
                    maze[i - 1][j] = "+"
                if j < len(maze[0]) - 1 and maze[i][j + 1] == ".":
                    temp.append([i, j + 1])
                    maze[i][j + 1] = "+"
                if j > 0 and maze[i][j - 1] == ".":
                    temp.append([i, j - 1])
                    maze[i][j - 1] = "+"
            queue = temp
            count += 1
        return -1


print(
    Solution().nearestExit(
        maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]],
        entrance=[1, 0],
    )
)

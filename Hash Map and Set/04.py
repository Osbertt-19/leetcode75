class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        i = 0
        p = 0
        for i in range(len(grid)):
            j = 0
            for j in range(len(grid[0])):
                b = True
                for k in range(len(grid)):
                    if grid[i][k] != grid[k][j]:
                        b = False
                        break
                if b:
                    p += 1
        return p


print(Solution().equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))

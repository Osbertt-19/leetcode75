from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        self.d = defaultdict(dict)
        for eq, val in zip(equations, values):
            self.d[eq[0]][eq[1]] = val
            self.d[eq[1]][eq[0]] = 1 / val
        ret = []
        for q in queries:
            ret.append(self.solve(q[0], q[1], 1, set()))
        return ret

    def solve(self, upper, lower, k, visited):
        if lower in self.d[upper]:
            return k * self.d[upper][lower]
        for neighbour in self.d[upper]:
            if not neighbour in visited:
                visited.add(neighbour)
                result = self.solve(
                    neighbour,
                    lower,
                    k * self.d[upper][neighbour],
                    visited,
                )
                if result != -1:
                    return result
        return -1


print(
    Solution().calcEquation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
)

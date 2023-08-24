class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
        for n in arr:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        a = []
        for n in d:
            if d[n] in a:
                return False
            else:
                a.append(d[n])
        return True


print(Solution().uniqueOccurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        biggest = max(candies)
        bol = []
        for candy in candies:
            if candy + extraCandies >= biggest:
                bol.append(True)
            else:
                bol.append(False)
        return bol


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 3, 4, 1], 3))

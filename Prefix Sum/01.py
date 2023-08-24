class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i - 1]
        gain.append(0)
        return max(gain)


print(Solution().largestAltitude([-5, 1, 5, 0, -7]))

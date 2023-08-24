class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        p1 = 0
        p2 = k
        mx = float("-inf")
        sum = 0
        for i in range(k):
            sum = sum + nums[p1 + i]
        mx = sum
        while p2 < len(nums):
            sum = sum + nums[p2] - nums[p1]
            if sum > mx:
                mx = sum
            p1 = p1 + 1
            p2 = p2 + 1
        return mx / k


sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))

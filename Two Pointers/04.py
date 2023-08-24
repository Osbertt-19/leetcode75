class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        total = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                total = total + 1
                left = left + 1
                right = right - 1
            elif sum > k:
                right = right - 1
            else:
                left = left + 1
        return total


sol = Solution()
print(sol.maxOperations([3, 1, 3, 4, 3], 6))

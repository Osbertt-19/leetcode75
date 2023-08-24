class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumr = sum(nums[1:])
        suml = 0
        if sumr == suml:
            return 0
        p = 1
        while p < len(nums):
            sumr -= nums[p]
            suml += nums[p - 1]
            if sumr == suml:
                return p
            p += 1
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        nums.insert(0, 0)
        nums.append(0)
        indexes = []
        p = 0
        while p < len(nums) and len(indexes) != k + 2:
            if nums[p] == 0:
                indexes.append(p)
            p = p + 1
        mx = indexes[-1] - indexes[0] - 1
        while p < len(nums):
            if nums[p] == 0:
                indexes = indexes[1:] + [p]
                if mx < indexes[-1] - indexes[0] - 1:
                    mx = indexes[-1] - indexes[0] - 1
            p = p + 1
        return mx


sol = Solution()
print(sol.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))

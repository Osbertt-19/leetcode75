class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
        print(nums)


sol = Solution()
sol.moveZeroes([0, 1, 2, 5, 0, 0, 4])

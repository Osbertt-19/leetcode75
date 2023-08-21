class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        for num in nums:
            product = product * num
        ret = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ret.append(product // nums[i])
            else:
                app = 1
                for j in range(len(nums)):
                    if i != j:
                        app = app * nums[j]
                ret.append(app)
        return ret


sol = Solution()
print(sol.productExceptSelf([-1, -3, 0, 1, 3]))

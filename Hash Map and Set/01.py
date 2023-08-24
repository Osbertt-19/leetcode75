class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [
            list(s1.difference(s2)),
            list(s2.difference(s1)),
        ]


print(Solution().findDifference([1, 2, 3, 4], [3, 4, 5, 6]))

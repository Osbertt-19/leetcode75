class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = float("-infinity")
        while left < right:
            print(left, right)
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            if max_area < area:
                max_area = area
            if height[left] < height[right]:
                left = left + 1
            elif height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
                right = right - 1
            print(left, right, max_area)
        return max_area


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 500, 100, 8, 3, 7]))

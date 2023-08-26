class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break
            else:
                if not stack or stack[-1] < 0 or a > 0:
                    stack.append(a)
        return stack


print(Solution().asteroidCollision([1, 2, 4, -3]))

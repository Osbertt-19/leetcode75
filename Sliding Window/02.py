class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        p1 = 0
        p2 = k
        mx = float("-inf")
        sum = 0
        for i in range(k):
            if s[p1 + i] in vowels:
                sum = sum + 1
        mx = sum
        while p2 < len(s):
            if s[p2] in vowels:
                sum = sum + 1
            if s[p1] in vowels:
                sum = sum - 1
            if mx < sum:
                mx = sum
            p1 = p1 + 1
            p2 = p2 + 1
        return mx


sol = Solution()
print(sol.maxVowels("abciidef", 3))

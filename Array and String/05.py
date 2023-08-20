class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        rev = []
        str = list(s)
        for letter in s:
            if letter in vowels:
                rev.append(letter)
        i = 0
        while i < len(s):
            if s[i] in vowels:
                str[i] = rev.pop()
            i = i + 1
        return "".join(str)


sol = Solution()
print(sol.reverseVowels("AaAA"))

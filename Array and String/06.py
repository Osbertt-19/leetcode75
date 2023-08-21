class Solution:
    def reverseWords(self, s: str) -> str:
        s = s + " "
        word = ""
        words = []
        for letter in s:
            if letter != " ":
                word = word + letter
            else:
                if word != "":
                    words.insert(0, word)
                    word = ""
        print(words)
        return " ".join(words)


sol = Solution()
print(sol.reverseWords("   i am    a student"))

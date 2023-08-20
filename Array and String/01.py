class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        p = 0
        while p < len(word1) and p < len(word2):
            result = result + word1[p]
            result = result + word2[p]
            p = p + 1
        print(word1[len(word2) :])
        print(word2[len(word1) :])
        result = result + word1[len(word2) :]
        result = result + word2[len(word1) :]
        return result

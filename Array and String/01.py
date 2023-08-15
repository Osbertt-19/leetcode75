class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            result = result + word1[p1]
            result = result + word2[p2]
            p1 = p1 + 1
            p2 = p2 + 1
        print(word1[len(word2) :])
        print(word2[len(word1) :])
        result = result + word1[len(word2) :]
        result = result + word2[len(word1) :]
        return result

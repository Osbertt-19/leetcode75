class Solution:
    def compress(self, chars: list[str]) -> int:
        ret = ""
        c = ""
        n = 0
        for char in chars:
            if char == c:
                n = n + 1
            else:
                if n > 1:
                    ret = ret + c + str(n)
                else:
                    ret = ret + c
                c = char
                n = 1
        if n > 1:
            chars = list(ret + c + str(n))
        else:
            chars = list(ret + c)
        print(chars)
        return len(chars)


sol = Solution()
print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

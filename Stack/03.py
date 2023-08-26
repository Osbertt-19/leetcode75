class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == "[":
                stack.append(cur_num)
                stack.append(cur_str)
                cur_num = 0
                cur_str = ""
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                cur_str = prev_str + cur_str * prev_num
            else:
                cur_str += c
        while stack:
            cur_str = stack.pop() + cur_str

        return cur_str


print(Solution().decodeString("3[a]2[bc]"))

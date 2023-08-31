# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        i = len(s) // 2
        j = i - 1
        mx = float("-inf")
        while j >= 0:
            sm = s[i] + s[j]
            if sm > mx:
                mx = sm
            i += 1
            j -= 1
        return mx

# reverse Linked List
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        previous = head
        current = head.next
        while current is not None:
            head.next = current.next
            current.next = previous

            previous = current
            current = head.next

        return previous

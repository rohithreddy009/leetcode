from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(99, head)
        left = dummy
        right = head
        count = 0
        while right != None:
            right = right.next
            count += 1
            if count > n:
                left = left.next
        left.next = left.next.next
        return dummy.next
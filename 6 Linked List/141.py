# time: 0(n)    space: 0(1)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    



# time and space 0(n)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        set_ = set()
        curr = head
        while curr:
            if curr in set_:
                return True
            set_.add(curr)
            curr = curr.next
        return False

        
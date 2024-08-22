class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum_ = v1 + v2 + carry

            carry = sum_ // 10
            val = sum_ % 10
            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if carry:
                curr.next = ListNode(carry)
        
        return dummy.next
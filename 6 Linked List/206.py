class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to the next node in the original list
        return prev  # prev will be the new head of the reversed list



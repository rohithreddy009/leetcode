class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            dummyList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                dummyList.append(self.mergeList(l1, l2))
            lists = dummyList
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
        curr.next = l1 or l2
        return dummy.next
    
a = Solution()
print(a.mergeKLists([[1,4,5],[1,3,4],[2,6]]))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy = ListNode()

        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                node.next = p1
                node = node.next
                p1 = p1.next
            else:
                node.next = p2
                node = node.next
                p2 = p2.next

        node.next = p1 or p2
        return dummy.next
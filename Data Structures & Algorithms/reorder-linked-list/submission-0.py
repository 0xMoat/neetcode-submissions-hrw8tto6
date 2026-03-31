# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. revert right half nodes, prev will be the right half start
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        # 3. merge 2 linked list
        p1, p2 = head, prev
        while p2:
            temp1, temp2 = p1.next, p2.next
            p1.next = p2
            p2.next = temp1
            p1, p2 = temp1, temp2


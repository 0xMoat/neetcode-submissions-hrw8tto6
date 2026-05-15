# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. slow & fast pointer find out the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse right part linked list
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
        
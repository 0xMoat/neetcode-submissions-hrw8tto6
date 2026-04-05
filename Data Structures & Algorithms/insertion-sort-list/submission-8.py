# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        while cur:
            tmp = head
            while tmp != cur:
                if tmp.val > cur.val:
                    tmp.val, cur.val = cur.val, tmp.val
                tmp = tmp.next
            cur = cur.next
        return head


    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            temp = curr.next
            prev.next, curr.next = curr, prev.next
            curr = temp
        return dummy.next

        







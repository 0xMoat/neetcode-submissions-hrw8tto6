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
        dummy = ListNode(0)  # 虚拟头节点，方便插入

        cur = head
        while cur:
            prev = dummy  # 每次从头找插入位置

            # 找到第一个大于 cur.val 的位置
            while prev.next and prev.next.val < cur.val:
                prev = prev.next

            next_temp = cur.next  # 先保存下一个节点

            # 插入 cur 到 prev 后面
            cur.next = prev.next
            prev.next = cur

            # 继续处理原链表下一个节点
            cur = next_temp

        return dummy.next









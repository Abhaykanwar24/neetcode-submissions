# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        reverse_prev = None

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = reverse_prev
            reverse_prev = cur
            cur = next_node


        prev.next.next = cur     
        prev.next = reverse_prev

        return dummy.next






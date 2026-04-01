# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing second half
        prev , curr = None , slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l , r = head,prev
        while r:
            temp = l.next
            temp2 = r.next
            l.next = r
            r.next = temp
            l = temp
            r = temp2
        
        
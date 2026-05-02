# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: 
            return head
            

        l = head
        m = l.next

        if head.next.next is None:
            l.next = None
            m.next = l

            return m

        l.next = None
        r = m.next

        while r:
            m.next = l
            
            l = m
            m = r
            r = r.next
        
        m.next = l

        return m
            
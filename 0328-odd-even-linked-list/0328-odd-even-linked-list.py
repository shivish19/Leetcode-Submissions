# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        # Head of the even list to link at the end
        even_head = head.next
        
        # Pointers to traverse the odd and even nodes
        odd = head
        even = even_head

        while even and even.next:
            # Connect the next odd node
            odd.next = even.next
            odd = odd.next
            
            # Connect the next even node
            even.next = odd.next
            even = even.next

        # Connect the end of the odd list to the head of the even list
        odd.next = even_head

        return head

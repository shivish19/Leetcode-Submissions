# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head is None or head.next==None:
            return head

        dummy=ListNode(0)
        dummy.next=head
        front=dummy
        right_head=head
        
        for _ in range(1,left):
            front=front.next
        
        left_head=front.next

        for _ in range(1,right):
            right_head=right_head.next

        tail=right_head.next


        ptr=left_head
        prev=None
        while prev!=right_head:
            temp=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=temp

        prev=right_head

        front.next=right_head
        left_head.next=tail



        return dummy.next
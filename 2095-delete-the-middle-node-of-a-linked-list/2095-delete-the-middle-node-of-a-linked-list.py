# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None

        f=head
        s=head
            

        while f and f.next:
            f=f.next.next
            temp=s
            s=s.next

        temp.next=s.next

        return head



        
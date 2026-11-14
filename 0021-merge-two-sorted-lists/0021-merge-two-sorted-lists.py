# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # list1-head1
        # list2-head2
        # Brute
        dummy=ListNode(-1)
        head=dummy
        ptr1=list1
        ptr2=list2
        while ptr1 or ptr2:

            if ptr1 and ptr2 and ptr1.val<=ptr2.val:
                head.next=ListNode(ptr1.val)
                head=head.next
                ptr1=ptr1.next

            elif ptr2==None:
                head.next=ListNode(ptr1.val)
                head=head.next
                ptr1=ptr1.next

            elif ptr1==None:
                head.next=ListNode(ptr2.val)
                head=head.next
                ptr2=ptr2.next

            else:
                head.next=ListNode(ptr2.val)
                head=head.next
                ptr2=ptr2.next
                
        return dummy.next
        
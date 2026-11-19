# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        temp=head
        l=0
        while temp:
            l+=1
            temp=temp.next
        
        mid=l//2
        
        s=head
        while mid:
            mid-=1
            s=s.next
        
        return s
            

        
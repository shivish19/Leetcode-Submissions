# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head
        t=head
        l=[]
        while t:
            l.append(t.val)
            t=t.next
        
        # now ques-rotate array to right
        n=len(l)
        k=k%n
        if k==0:
            return head

        
        res=l[n-k:]+l[:n-k]
        
        dummy=ListNode(-1)
        head=dummy
        for v in res:
            head.next=ListNode(v)
            head=head.next
        

        return dummy.next

        
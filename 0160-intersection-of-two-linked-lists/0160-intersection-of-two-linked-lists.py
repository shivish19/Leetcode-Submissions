# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def collision(h1,h2,d):

            while d:
                d-=1
                h2=h2.next
            
            while h1!=h2:
                h1=h1.next
                h2=h2.next
            
            return h1
        
        t1=headA
        t2=headB

        n1=n2=0

        # length of l1-
        while t1:
            n1+=1
            t1=t1.next

        while t2:
            n2+=1
            t2=t2.next
        
        if n1<n2:
            return collision(headA,headB,n2-n1)
        else:
            return collision(headB,headA,n1-n2)
                

            
        
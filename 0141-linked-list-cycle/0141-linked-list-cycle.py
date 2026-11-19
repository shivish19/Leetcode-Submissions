# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        hm={}
        while temp:
            if temp in hm:
                return True

            hm[temp]=1
            temp=temp.next

        return False
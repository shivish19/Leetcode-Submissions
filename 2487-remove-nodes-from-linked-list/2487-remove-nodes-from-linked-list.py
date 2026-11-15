# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        stack=[]
        vals=[]
        temp=head
        while temp:
            vals.append(temp.val)
            temp=temp.next

        for i in range(len(vals)):
            while stack and stack[-1]<vals[i]:
                stack.pop()

            stack.append(vals[i])

        dummy=ListNode(-1)
        head=dummy

        for val in stack:
            head.next=ListNode(val)
            head=head.next

        return dummy.next




            
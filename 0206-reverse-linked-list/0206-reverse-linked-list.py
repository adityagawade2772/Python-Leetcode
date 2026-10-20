# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            e = stack.pop()
            temp.val = e
            temp = temp.next

        return  head

        
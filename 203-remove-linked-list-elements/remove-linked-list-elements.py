# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dumm=ListNode()
        temp2=dumm
        temp=head
        while temp:
            if temp.val!= val:
                dumm.next=temp
                dumm=dumm.next
            temp=temp.next
        dumm.next=None
        return temp2.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
     if not head or not head.next:
            return head
     else:
        l=1
        temp=head
        while temp.next:
            l+=1
            temp=temp.next
        k=k%l
        r=l-k
        for i in range(r):
            temp.next=head
            head=head.next
            temp.next.next=None
            temp=temp.next
            
        return head
         
        
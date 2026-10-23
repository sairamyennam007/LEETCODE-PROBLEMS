# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        f=head
        while f and f.next:
            swap2=f
            swap1=f.next
            f=f.next.next
            swap2.next=f
            swap1.next=swap2
            prev.next=swap1
            prev=prev.next.next
        return dummy.next




            
        
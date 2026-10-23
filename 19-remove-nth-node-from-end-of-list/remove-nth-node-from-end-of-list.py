# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        pos=l-n+1
        if pos==1:
            head=head.next
        else:
         temp2=head
         for i in range(1,pos-1):
            temp2=temp2.next
         temp2.next=temp2.next.next
        return head
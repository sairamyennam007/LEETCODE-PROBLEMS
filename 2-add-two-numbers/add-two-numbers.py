# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry=0
        dummy=ListNode(0)
        temp=dummy
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=x+y+carry
            s1=ListNode(s%10)
            temp.next=s1
            temp=temp.next
            carry=s//10
            if l1:
              l1=l1.next
            if l2:
              l2=l2.next
        return dummy.next
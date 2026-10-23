# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dumm = ListNode(0)
        temp = dumm
        bar = False

        while l1 and l2:
            s = l1.val + l2.val

            if bar:
                s += 1

            if s < 10:
                s1 = ListNode(s)
                bar = False
            else:
                s1 = ListNode(s % 10)
                bar = True

            temp.next = s1
            temp = temp.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val

            if bar:
                s += 1

            if s < 10:
                s1 = ListNode(s)
                bar = False
            else:
                s1 = ListNode(s % 10)
                bar = True

            temp.next = s1
            temp = temp.next
            l1 = l1.next

        while l2:
            s = l2.val

            if bar:
                s += 1

            if s < 10:
                s1 = ListNode(s)
                bar = False
            else:
                s1 = ListNode(s % 10)
                bar = True

            temp.next = s1
            temp = temp.next
            l2 = l2.next

        if bar:
            temp.next = ListNode(1)

        return dumm.next
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        d={}
        while temp:
            d[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            n=d[temp]
            n.next=d.get(temp.next,None)
            n.random=d.get(temp.random,None)
            temp=temp.next
        return d.get(head,None)

        
        
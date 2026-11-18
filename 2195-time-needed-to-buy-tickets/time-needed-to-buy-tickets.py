from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        t=0
        for i in range(len(tickets)):
            if i<k:
                t+=min(tickets[i],tickets[k])
            elif i==k:
                t+=tickets[k]
            else:
                if tickets[i]>=tickets[k]:
                  t+=tickets[k]-1
                else:
                    t+=tickets[i]
                
        return t



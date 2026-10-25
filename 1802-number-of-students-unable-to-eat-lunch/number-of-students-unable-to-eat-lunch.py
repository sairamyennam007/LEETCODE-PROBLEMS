from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        i=0
        q=deque(students)
        c=0
        while q and c<len(q):
            if q[0]==sandwiches[i]:
                i+=1
                q.popleft()
                c=0
            else:
                c+=1
                q.append(q.popleft())

        return c
               
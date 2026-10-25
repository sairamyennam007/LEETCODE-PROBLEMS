class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        c0=students.count(0)
        c1=students.count(1)
        for num in sandwiches:
            if num==0 and c0==0:
                return c1
            elif num==1 and c1==0:
                return c0
            elif num==0:
                c0-=1
            else:
                c1-=1
        return c0+c1
        
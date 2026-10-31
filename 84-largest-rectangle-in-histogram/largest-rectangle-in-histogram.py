class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxarea=0
        stk=[]
        stk2=[]
        n=len(heights)
        rstk=[n]*n
        lstk=[-1]*n
        for i in range(len(heights)):
            if not stk:
                stk.append(i)
            else:
                while stk and heights[i]<heights[stk[-1]]:
                    rstk[stk.pop()]=i
                stk.append(i)
            if not stk2:
                stk2.append(i)
            else:
                while stk2 and heights[i]<=heights[stk2[-1]]:
                    stk2.pop()
                if stk2:
                    lstk[i]=stk2[-1]
                stk2.append(i)
        for i in range(n):
            width = rstk[i] - lstk[i] - 1
            area = heights[i] * width
            maxarea=max(maxarea,area)
        return maxarea





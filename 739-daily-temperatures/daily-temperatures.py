class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res=len((temperatures))*[0]
        stk=[]
        for i in range(len(temperatures)):
            while stk and temperatures[i]>temperatures[stk[-1]]:
                idx=i-stk[-1]
                res[stk.pop()]=idx
            stk.append(i)
        return res

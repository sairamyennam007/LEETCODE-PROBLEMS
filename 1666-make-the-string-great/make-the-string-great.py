class Solution:
    def makeGood(self, s: str) -> str:
        stk=[]
        for num in s:
            if  stk and num!=stk[-1] and num.lower()==stk[-1].lower():
                stk.pop()
            else:
                stk.append(num)    
        return "".join(stk)
        
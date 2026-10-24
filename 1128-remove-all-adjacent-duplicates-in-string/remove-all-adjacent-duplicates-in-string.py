class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk=[]
        for num in s:
            if not stk:
                stk.append(num)
            elif stk[-1]==num:
                stk.pop()
            else:
                stk.append(num)

        return "".join(stk)
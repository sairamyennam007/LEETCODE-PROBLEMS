class Solution:
    def makeGood(self, s: str) -> str:
        stk=[]
        for num in s:
            if not stk:
                stk.append(num)
            else:
                    if num.isupper() == stk[-1].isupper():
                        stk.append(num)
                    elif num.islower()==stk[-1].islower():
                        stk.append(num)
                    elif num.upper() != stk[-1].upper():
                        stk.append(num)
                    else:
                        stk.pop()
        return "".join(stk)
        
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk=[]
        for num in tokens:
            if num not in "+-*/":
                stk.append(int(num))
            else:
                a=stk.pop()
                b=stk.pop()
                if num=='+':
                    stk.append(a+b)
                elif num=='-':
                     stk.append(b-a)
                elif num=='/':
                    stk.append(int(b/a))

                else:
                    stk.append(int(a*b))
        return stk[-1]

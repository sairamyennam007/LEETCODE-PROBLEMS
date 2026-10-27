class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res=[]
        stk=[]
        for i in range(len(tokens)):
            if stk and not tokens[i].lstrip("-").isdigit():
                b=stk.pop()
                a=stk.pop()
                if tokens[i]=="+":
                    stk.append(a+b)
                elif tokens[i]=="-":
                    stk.append(a-b)
                elif tokens[i]=="*":
                    stk.append(a*b)
                else:
                    res=abs(a)//abs(b)
                    if (a<0)!=(b<0):
                        res=-res
                    stk.append(res)    
            else:
                stk.append(int(tokens[i]))
        return stk[0]

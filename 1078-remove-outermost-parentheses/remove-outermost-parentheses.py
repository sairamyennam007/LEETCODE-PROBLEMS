class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        c=0
        stk=[]
        stk2=[]
        for num in s:
            if num in "(":
                stk.append(num)
                stk2.append(num)
            else:
                stk2.append(num)
                c+=1
                if c==len(stk):
                    res+="".join(stk2[1:len(stk2)-1])
                    stk2.clear()
                    stk.clear()
                    c=0
        return res


               
        return res


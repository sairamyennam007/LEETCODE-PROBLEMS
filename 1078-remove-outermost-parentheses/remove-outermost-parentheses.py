class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        res=[]
        for num in s:
            if num in "(":
                c+=1
                if c>1:
                    res.append(num)
                
            else:
                c-=1
                if c!=0:
                    res.append(num)
                
        return "".join(res)


            
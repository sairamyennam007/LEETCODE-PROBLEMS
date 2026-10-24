class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        res=""
        for num in s:
            if num in "(":
                c+=1
                if c>1:
                    res+=num
                
            else:
                c-=1
                if c!=0:
                    res+=num
                
        return res


            
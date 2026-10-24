class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        d={")":"(","}":"{","]":"["}
        for num in s:
            if num in  "({[":
                stk.append(num)

            else:
              if not stk or stk[-1]!=d[num]:
                return False
              stk.pop()
                
             
        return len(stk)==0
        

        
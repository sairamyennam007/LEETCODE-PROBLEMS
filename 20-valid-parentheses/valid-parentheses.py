class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        d={")":"(","}":"{","]":"["}
        for num in s:
            if num in  "({[":
                stk.append(num)

            else:
              if stk:
                if d[num]==stk[-1]:
                    stk.pop()
                else:
                    return False
              else:
                    return False

        return len(stk)==0
        

        
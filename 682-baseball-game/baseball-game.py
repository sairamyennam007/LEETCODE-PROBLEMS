class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk=[]
        for i in range(len(operations)):
            
                
            if operations[i] == '+':
                stk.append(stk[-1]+stk[-2])
            elif operations[i]=='D':
                stk.append(stk[-1]*2)
            elif operations[i]=='C': 
                stk.pop()
            else:
                stk.append(int(operations[i]))

        return sum(stk)
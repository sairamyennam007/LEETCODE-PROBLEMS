class Solution:
    def decodeString(self, s: str) -> str:
        cs=""
        alp=[]
        val=[]
        n=0
        for num in s:
            if num=='[':
                val.append(n)
                alp.append(cs)
                cs=""
                n=0
            elif num.isdigit():
                n=n*10+int(num)
            elif num.isalpha():
                cs+=num
            else:
                cs=alp.pop()+cs*int(val.pop())
        return cs
               
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        l=len(s)
        l1=len(t)
        if l==l1:
         i=0
         while i<l:
            if s[i]==t[i]:
                i+=1
            else:
                return False
        else:
            return False
        return True
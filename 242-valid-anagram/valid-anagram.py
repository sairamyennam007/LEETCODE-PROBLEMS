class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for num in s:
            d[num]=d.get(num,0)+1
        for n in t:
            if  n not in d:
                return False
            d[n]-=1
            if d[n]<0:
                return False
        return True
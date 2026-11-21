class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        d={}
        w={}
        res=[]
        i=0
        j=0
        for num in p:
            d[num]=d.get(num,0)+1
        while j<len(s):
            w[s[j]]=w.get(s[j],0)+1
            while j-i+1==len(p):
                if w==d:
                    res.append(i)
                w[s[i]]-=1
                if w[s[i]]==0:
                    w.pop(s[i])
                i+=1
            j+=1
        return res
                

        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        m=0
        dic={}
        while j<len(s):
            if s[j] not in dic:
                dic[s[j]]=1
            else:
                dic[s[j]]+=1
            while  (j-i+1)-max(dic.values()) >k:
                dic[s[i]]-=1
                i+=1
            m=max(m,j-i+1)
            j+=1
        return m
                


         
            
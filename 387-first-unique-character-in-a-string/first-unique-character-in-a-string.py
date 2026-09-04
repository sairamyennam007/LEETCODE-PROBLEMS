class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1


        for j in range(len(s)):
           if dict[s[j]]==1:
             return j
        return -1

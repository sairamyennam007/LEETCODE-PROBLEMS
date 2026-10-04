class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic={}
        win={}
        for num in s1:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        i=0
        j=0
        while j<len(s2):
            if s2[j] not in win:
                win[s2[j]]=1
            else:
                 win[s2[j]]+=1
            if (j-i+1)==len(s1):
                if dic==win:
                    return True
                
                win[s2[i]]-=1
                if win[s2[i]]==0:
                    win.pop(s2[i])
                i+=1
            j+=1
        return False

        
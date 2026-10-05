class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=""
        i=0
        j=0
        dic={}
        win={}
        for num in t:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1

        while j<len(s):
            if s[j] not in win:
                win[s[j]]=1
            else:
                win[s[j]]+=1
            while all( dic[ch] <= win.get(ch,0) for ch in dic) :
                if ans=="" or (j-i+1)<len(ans):
                    ans=s[i:j+1]
                win[s[i]]-=1
                if win[s[i]]==0:
                    win.pop(s[i])
                i+=1
            j+=1
        return ans

        
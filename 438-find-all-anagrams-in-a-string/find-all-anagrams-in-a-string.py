class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        i=0
        j=0
        lt=[]
        dic={}
        win={}
        for num in p:
            if num not in dic:
                dic[num]=1
            else:
                 dic[num]+=1
        while j<len(s):
            if s[j] not in win:
                win[s[j]]=1
            else:
                win[s[j]]+=1
            while (j-i+1)==len(p):
                if win==dic:
                    lt.append(i)
                win[s[i]]-=1
                if win[s[i]]==0:
                    win.pop(s[i])
                i+=1
            j+=1
        return lt



            

            



           
        return lt

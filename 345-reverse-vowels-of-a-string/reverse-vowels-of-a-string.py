class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        l= list(s)
        while i<j:
            if l[i] in "aeiouAEIOU" and l[j] in "aeiouAEIOU":
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            while i<j and  l[i] not in "aeiouAEIOU":
                i+=1
            while i<j and  l[j] not in "aeiouAEIOU":
                j-=1
        return "".join(l)
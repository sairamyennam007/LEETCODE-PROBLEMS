class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        res=""
        for i in range(l):
            le,r=i,i
            while le>=0 and r<l and s[le]==s[r]:
              if r-le+1>len(res):
                 res=s[le:r+1]
              le-=1
              r+=1
            le,r=i,i+1
            while le>=0 and r<l and s[le]==s[r]:
                if r-le+1>len(res):
                  res=s[le:r+1]
                le-=1
                r+=1
        return res
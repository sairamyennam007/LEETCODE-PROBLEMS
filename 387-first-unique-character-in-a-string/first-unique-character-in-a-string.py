class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for num in s:
            d[num]=d.get(num,0)+1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
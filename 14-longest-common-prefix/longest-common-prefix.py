class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        st=strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(st):
                st=st[:-1]
            if st=="":
                return st
        return st
        
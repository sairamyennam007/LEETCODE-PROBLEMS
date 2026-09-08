class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=[]
        i=0
        j=0
        l=0
        while j<len(s):
            if s[j] not in st:
                st.append(s[j])
                l=max(l,j-i+1)
                j+=1
            else:
                i+=1
                st.pop(0)
        return l
                

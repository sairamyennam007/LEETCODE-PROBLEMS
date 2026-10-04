class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        m=0
        dic={1:0,0:0}
        i=0
        j=0
        while j<len(nums):
            dic[nums[j]]+=1
         
            while dic[0] > k:
                dic[nums[i]]-=1
                i+=1
            m=max(j-i+1,m)
            j+=1
        return m

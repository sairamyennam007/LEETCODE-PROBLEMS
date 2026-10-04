class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        m=0
        zero=0
        i=0
        j=0
        while j<len(nums):
            if nums[j]==0:
                zero+=1
         
            while zero > k:
                if nums[i]==0:
                    zero-=1
                i+=1
            m=max(j-i+1,m)
            j+=1
        return m

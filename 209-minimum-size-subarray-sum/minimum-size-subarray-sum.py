class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        s=0
        minlen=float('inf')
        while j<len(nums):
            s+=nums[j]
            while s>=target:
                minlen=min(j-i+1,minlen)
                s-=nums[i]
                i+=1
            j+=1
        if minlen !=float('inf'):
            return minlen
        return 0


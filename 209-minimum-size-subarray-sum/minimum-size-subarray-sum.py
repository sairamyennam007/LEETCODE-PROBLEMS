class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i=0
        sum=0
        minl=float('inf')
        for j in range(len(nums)):
            sum+=nums[j]
            
            while sum>=target:
                minl=min(minl,j-i+1)
                sum-=nums[i]
                i+=1
        if minl!=float('inf'):
            return minl
        else:
            return 0
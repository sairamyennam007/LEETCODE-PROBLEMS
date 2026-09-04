class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        s=0
        maxavg=float('-inf')
        while j<len(nums):
            s+=nums[j]
            if j-i+1==k:
                maxavg=max(maxavg,s/k)
                s-=nums[i]
                i+=1
            j+=1
        return maxavg
            
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        win=sum(nums[:k])
        maxi=win
        for j in range(k,len(nums)):
            win+=nums[j]
            win-=nums[j-k]

            maxi=max(maxi,win)
        return maxi/k
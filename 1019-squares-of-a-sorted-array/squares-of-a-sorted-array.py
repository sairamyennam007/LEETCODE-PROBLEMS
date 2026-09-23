class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i=0
        j=k=len(nums)-1
        lt=[0]*len(nums)
        while i<=j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                lt[k]=nums[i]*nums[i]
                i+=1
            else:
                lt[k]=nums[j]*nums[j]
                j-=1
            k-=1
        return lt
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix=[]
        pre=1
        suf=1
        for i in range(len(nums)):
            prefix.append(pre)
            pre*=nums[i]
        for j in range((len(nums)-1),-1,-1):
            prefix[j]*=suf
            suf*=nums[j]
        return prefix
       
        
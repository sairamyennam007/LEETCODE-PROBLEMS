class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        i=0
        while i<len(nums):
            cpos=nums[i]-1
            if nums[cpos]!=nums[i]:
                nums[i],nums[cpos]=nums[cpos],nums[i]
            else:
                i+=1
        res=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
            else:
                i+=1
        return res
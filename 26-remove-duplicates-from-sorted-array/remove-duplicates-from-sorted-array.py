class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=1
        j=1
        while i<=j and i<len(nums) and j<len(nums):
            if nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i+=1
            j+=1
        return i
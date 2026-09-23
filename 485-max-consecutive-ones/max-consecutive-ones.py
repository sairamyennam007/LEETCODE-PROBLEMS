class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        mx=0
        for num in nums:
            if num==1:
                c+=1
                mx=max(c,mx)
            else:
                c=0
        return mx
        
        
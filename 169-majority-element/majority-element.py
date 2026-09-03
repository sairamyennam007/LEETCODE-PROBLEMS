class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        guy=None
        c=0
        for num in nums:
            if c==0:
                guy=num
                c+=1
            elif num==guy:
                c+=1
            else:
                c-=1
        return guy
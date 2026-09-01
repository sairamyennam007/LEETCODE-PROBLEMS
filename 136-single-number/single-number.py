class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in  dict:
                dict[num]=0
            else:
                dict[num]+=1
        for n in nums:
            if dict[n]==0:
                return n
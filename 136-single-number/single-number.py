class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in  dict:
                dict[num]=0
            else:
                dict.pop(num)
        for n in dict:
            return n
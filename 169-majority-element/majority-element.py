class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        num1=0
        for num in nums:
            if c==0:
                num1=num
                c+=1
            else:
                if num==num1:
                    c+=1
                else:
                    c-=1
        return num1

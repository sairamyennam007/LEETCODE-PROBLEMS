class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d={}
        l=len(nums2)
        d={}
        stk=[]
        for n in nums2:
            d[n]=-1
        for num in nums2:
            if not stk:
                stk.append(num)
            else:
                while stk and num>stk[-1]:
                    d[stk.pop()]=num
                stk.append(num)
        for i in range(len(nums1)):
            nums1[i]=d[nums1[i]]
        return nums1



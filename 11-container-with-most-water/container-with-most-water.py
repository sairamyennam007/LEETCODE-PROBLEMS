class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]<height[j]:
                maxarea=max(maxarea,height[i]*(j-i))
                i+=1
            else:
                maxarea=max(maxarea,height[j]*(j-i))
                j-=1
        return maxarea            
        
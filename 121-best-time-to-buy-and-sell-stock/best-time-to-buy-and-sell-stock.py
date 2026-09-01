class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float('inf')
        pro=0
        for i in range(len(prices)-1):
            if prices[i]<min:
                min=prices[i]
            if prices[i+1]-min >pro:
                pro=prices[i+1]-min
        return pro


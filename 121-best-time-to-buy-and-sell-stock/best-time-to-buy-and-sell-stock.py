class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        pro=0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            if prices[i]-mini >pro:
                pro=prices[i]-mini
        return pro


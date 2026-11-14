dp={}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        if n in dp:
            return dp[n]
        dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return dp[n]
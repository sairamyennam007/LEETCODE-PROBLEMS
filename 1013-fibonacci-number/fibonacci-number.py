d={}
class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        if n in d:
            return d[n]
        d[n]=self.fib(n-1)+ self.fib(n-2)
        return d[n]
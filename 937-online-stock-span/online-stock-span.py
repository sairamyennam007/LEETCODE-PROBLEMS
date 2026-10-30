class StockSpanner:

    def __init__(self):
        self.stk=[]
    def next(self, price: int) -> int:
        c=1
        if not self.stk:
            self.stk.append([price,c])
        else:
            r=price
            while self.stk and self.stk[-1][0]<=r:
                c+=self.stk.pop()[1]
            self.stk.append([price, c])
        return c
    




        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stk=[]
        for num in asteroids:

                while stk and stk[-1]>0 and num<0:
                    if stk[-1]<abs(num):
                        stk.pop()
                    elif  stk[-1]==abs(num):
                        stk.pop()
                        break
                    else:
                        break
                else:
                    stk.append(num)
        return stk
class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.squares(n)
            if n==1:
                return True
        return False

    def squares(self,num):
        output=0
        while num:
            digit=num%10
            output+=digit**2
            num=num//10
        return output
        
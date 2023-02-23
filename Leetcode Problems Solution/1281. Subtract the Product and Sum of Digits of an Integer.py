class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        s=0
        while n>0:
            rem=n%10
            mul=mul*rem
            s=s+rem
            n=n//10
        res=mul-s
        return res    

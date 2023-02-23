class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        rev=0
        if x<0:
            sign=-1
            x=x*-1
        while x!=0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if not -2147483648<rev<2147483648:
            return 0
        return (rev *sign )   
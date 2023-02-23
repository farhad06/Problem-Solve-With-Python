class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:return False
        s=0
        temp=x
        while x !=0:
            rem=x%10
            s=s*10+rem
            x=x//10
        if s==temp:
            return True
        else:
            return False   
class Solution:
    def isHappy(self, n: int) -> bool:
      st=set()
      while n not in st:
          st.add(n)
          n=self.countDigits(n)
          if n==1:
              return True
      return False        
    def countDigits(self,n:int) ->int:
        s=0
        while n>0:
            rem=n%10
            s=s+rem**2
            n=n//10
        return s 
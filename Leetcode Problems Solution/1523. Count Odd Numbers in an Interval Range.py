class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        if low % 2==0:
            low+=1
        if high %2 ==0:
            high-=1
        count=((high-low)//2)+1        
        return count
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr=list(t)
        for i in range(len(s)):
            arr.remove(s[i])
        return arr[0]    

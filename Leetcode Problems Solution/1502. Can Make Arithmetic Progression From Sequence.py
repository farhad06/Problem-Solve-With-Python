class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)==2:
            return True
        arr.sort()
        diff=arr[1]-arr[0]
        for i in range(2,len(arr)):
            countDiff=arr[i]-arr[i-1]
            if diff !=countDiff:
                return False
        return True
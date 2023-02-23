class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarr=[]
        s=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n+1):
                subarr.append(arr[i:j])
        # return subarr
        for i in subarr:
            if len(i) %2 !=0:
                s=s+sum(i)
        return s        

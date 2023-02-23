class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        mid=n//2
        s=0
        for i in range(n):
            s=s+mat[i][i]
            s=s+mat[n-1-i][i]
        if n %2==1:
            s=s-mat[mid][mid]
        return s        
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        size=m*n
        if r*c != size:
            return mat
        res=[[0 for i in range(c)]for j in range(r)]    
        for i in range(size):
            res[i//c][i%c]=mat[i//n][i%n]
        return res    

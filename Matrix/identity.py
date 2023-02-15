def isIdentity(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j and matrix[i][j]!=1:
                return False
            elif i!=j and matrix[i][j]!=0:
                return False
    return True 

mat=[[1,0,0],[0,1,0],[0,0,1]]
print("Entered matrix is: ")
for ele in mat:
    print(ele)


if isIdentity(mat):
    print("Matrix is a Identity matrix.")
else:
    print("Matrix is not Indentity matrix.")    

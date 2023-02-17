def sum(mat):
    s=0
    for i in range(len(mat)):
        s=s+mat[i][i] 
    return s 


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("Inputed Matrix is: ")
for ele in matrix:
    print(ele)

print("Sum of Left Diagonal Elements is:",sum(matrix))    
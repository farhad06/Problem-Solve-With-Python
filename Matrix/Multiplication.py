a=[[1,2,3],[4,5,6]]
b=[[7,8,9],[10,11,12]]
c=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]

print("New Matrix is: ")
for i in c:
    print(i) 
a=[[1,2],[4,5],[7,9]]
c=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[j][i]=a[i][j]


print("Original Matrix is: ")
for ele in a:
    print(ele)

print("Transpose Matrix is: ")
for i in c:
    print(i)        
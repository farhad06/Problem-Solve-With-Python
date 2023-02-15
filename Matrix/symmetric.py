def isSymmetric(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if (a[i][j] != a[j][i]):
                return False
    return True             


a=[[1, 3, 5], [3, 2, 4], [5, 4, 1]]

# flag=False 
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         if a[i][j]==a[j][i]:
#             flag=True
#             break

print("Entered matrix is: ")
for ele in a:
    print(ele) 

if isSymmetric(a):
    print("Entered matrix is Symmetric.")
else:
    print("Entered matrix is not Symmetric.")



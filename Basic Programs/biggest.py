n1=int(input("Enter the First number "))
n2=int(input("Enter the Second number "))
n3=int(input("Enter the Third number "))

if(n1>=n2) and (n1>=n3):
    big=n1
elif(n2>=n1) and (n2>=n3):
    big=n2
else:
    big=n3        
print("\nThe biggest number is: ",big)                        
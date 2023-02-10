import math 

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

if a==0:
    print("Invalid Input !")
d=b*b-4*a*c 

value_of_d=math.sqrt(abs(d))

if d>0:
    print("Roots are Real and Unequale: ")
    print(int((-b+value_of_d)/2*a))
    print(int((-b-value_of_d)/2*a))
 
elif d==0:
    print("Roots are Real and Equal: ")
    print(int(-b/2*a))
else:
    print("Roots are complex and Unequle: ") 
    print(-b/2*a,"+i",value_of_d/2*a)
    print(-b/2*a,"-i",value_of_d/2*a) 

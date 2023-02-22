'''a=[1,2,3]
try:
    print("Second element is: ", a[1])
    print("First element is: ", a[0])
except IndexError:
    print("Error occured ") 
else:
    print("Third element is: ", a[2])
finally:
    print("This line printed always")

a=int(input("Enter the 1st number\n"))
b=int(input("Enter the 2nd number\n"))

try:
    k=a/b
except ZeroDivisionError:
    print("Division by zero") 
else:
    print(k)  '''
    
         
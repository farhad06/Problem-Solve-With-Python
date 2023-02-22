def func():
    print("This is a function")
func()
#parametarized function
def add(a,b):
    return a+b
print("Sum of this two numbers is: ",add(2,5))
def student(name,roll):
    print("Name is: ",name,"Roll is:",roll)
student("Pant",77)
#default parameter
def mul(m,n=5):
    return m*n
print("Multiplication is: ",mul(5,3))

###lambda function
''' A lambda is a small anonymous function
syntax:---> lambda argument:expression
'''
x= lambda a,b,c:a+b+c
print("Sum is: ",x(1,2,3))
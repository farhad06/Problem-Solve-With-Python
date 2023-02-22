'''Syntax error::=> It are the problem in a program due to which the program will stop the execution.
                    It is caused by wrong syntax in the code.
   Exception::::=>  It are raised when some internal events occure which changes the normal flow of the program.
                    It are raised when the programs are syntactically correct but the code resulted in an error.
'''
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
try:
    div=a//b
    print("Division is: ",div)
except Exception as e:
    print("The problem is: ",e)
finally:
    print("It is always run")

###multiple error
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("B is: ",b)
except (ZeroDivisionError,NameError):
    print("Error occured")
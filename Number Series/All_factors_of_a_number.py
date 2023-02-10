from math import sqrt
def isFactor(num):
    lst=[]
    for i in range(1,int(sqrt(num)+1)):
        print(i)
        if num % i==0:
            lst.append(int(num/i))
    print("The Factors of " + str(num) + " are: ")
    for i in lst[::-1]:
        print(i,end=" ") 
n=int(input("Enter a number: "))
isFactor(n)               

def calculateFactor(n):
    i=1
    while i<=n: 
        if n %i ==0:
            print(i,end=" ")
        i+=1
num=int(input("Enter a Number. "))
print("Divisor of "+str(num)+" are. ") 

calculateFactor(num)
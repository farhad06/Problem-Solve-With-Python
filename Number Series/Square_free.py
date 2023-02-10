"""Given a number, check if it is square-free or not. A number is said to be square-free if no prime factor divides it more than once, i.e., the largest power of a prime factor that divides n is one"""
from math import sqrt
def isSquareFree(n):
	
	if n % 2 == 0:
		n = n / 2

	if n % 2 == 0:
		return False

	for i in range(3, int(sqrt(n) + 1)):
		if n % i == 0:
			n = n / i

		if n % i == 0:
			return False
	return True

n=int(input("Enter a number: "))

if isSquareFree(n):
    print("This is a Square Free Number. ")
else:
    print("This is not a Square free Number. ")

class Sum:
    def sum(self,a,b):
        return a+b;
class Sub:
    def sub(self,a,b):
        return a-b;
class Mul:
    def mul(self,a,b):
        return a*b;
class Dev:
    def dev(self,a,b):
        return a//b;
class Calculation(Sum,Sub,Mul,Dev):
    def mod(self,a,b):
        return a%b;
cal=Calculation()
print("Sum is: ",cal.sum(5,6))
print("Subtraction is: ",cal.sub(10,4))
print("Multiplication is: ",cal.mul(5,6))
print("Devition is: ",cal.dev(6,3))
print("Modulus is: ",cal.mod(6,4))


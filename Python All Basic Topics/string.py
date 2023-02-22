a="Hello,World" #initialized single line string
print(a) #print
multi_line='''However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.'''#Innitialized multi line string
print(multi_line)#print
print("****************************************************************************************************")
#access using for loop
fruit="banana"
for i in fruit:
    print(i)
print("*********************************************************************")
# convert upper case
print(fruit.upper())
## convert lower case
txt="HELLO"
print(txt.lower())
##remove any whitespace
txt1=" Hello"
print(txt1.strip())
print(txt1.rstrip())
##split string
txt2="H,e,l,l,o"
print(txt2.split(","))
print(txt2.rsplit(","))
##replace
st="Kolkata"
print(st.replace('K','J'))
#capitalized :convert the first letter in to upper case
name="farhad"
print(name.capitalize())
##convert string into lower case
name1="FARHAD"
print(name1.casefold())
#return the center position string
#print(name.center())
#find a sub string in a string
strings="This is a examle of string"
print(strings.find("is"))
print(strings.rfind("is"))
#convert each sub string into first letter
print(strings.title())
#join string
myTuple = ("John", "Peter", "Vicky")

x = "---->".join(myTuple)

print(x)
#swap case means lower to upper and upper to lower
n="this is the NAME"
print(n.swapcase())
##format string
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1);print(txt2);print(txt3)
#index
txt4="farhad ahamed"
print(txt4.index("h"))
#count a charccter
print(txt4.count('a'))

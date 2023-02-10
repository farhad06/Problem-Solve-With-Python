def convert(txt):
    for i in range(len(txt)):
        if txt[i] >='a' and txt[i]<='z':
            txt[i]=chr(ord(txt[i])-32)
        elif txt[i] >='A' and txt[i]<='Z':
            txt[i]=chr(ord(txt[i])+32)



string=input("Enter a string: ")
string=list(string)
convert(string)
string="".join(string)
print("Coverted string is:",string)
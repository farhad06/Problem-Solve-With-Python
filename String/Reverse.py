def rev(txt):
    new_txt=''
    for i in txt:
        new_txt=i+new_txt
    return new_txt 


txt=input("Enter a string: ")
print("The reverse string is: ",rev(txt))
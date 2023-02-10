string1=input("Enter the 1st string. ")
string2=input("Enter the 2nd string. ")

txt=""
if len(string1)>len(string2):
    for i in string1:
        if i not in string2:
            txt=txt+i 
else:
    print("Enter 1st string is bigger than string 2.")            

print("Final String is:",txt)            

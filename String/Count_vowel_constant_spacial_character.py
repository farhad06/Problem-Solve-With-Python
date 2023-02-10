def count(txt):
    vowel=0
    constant=0
    spacial_character=0
    digit=0
    space=0

    for i in range(len(txt)):
        ch=txt[i]
        if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
            ch=ch.lower()
            if ch=='a' or ch=='e' or ch=='i' or ch =='o' or ch=='u':
                vowel+=1
            else:
                constant+=1
        elif (ch>='0' and ch<='9'):
            digit+=1
        elif (ch ==" "):
            space+=1    
        else:
            spacial_character+=1 
    return vowel,constant,digit,spacial_character ,space

txt=input("Enter a String: ")
vowel,const,digits,char,space=count(txt)
print(f" No of vowel is:{vowel}\n No of constant is: {const}\n No of Digits is: {digits}\n No of Spacial Character is:{char}\n No of Space is:{space}")                            
def remove(txt):
    new_txt=""
    for i in txt:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            new_txt=new_txt+i 
        else:
            continue 
    return new_txt 


txt=input("Enter a string: ")
print("New Sentence is:",remove(txt))
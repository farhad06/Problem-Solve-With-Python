def removeSpace(txt):
    new_txt=""
    for i in txt:
        if i==" ":
            continue
        else:
            new_txt=new_txt+i  
    return new_txt

sentance=input("Enter a Sentance. ")
print("Sentance without space is:",removeSpace(sentance))            

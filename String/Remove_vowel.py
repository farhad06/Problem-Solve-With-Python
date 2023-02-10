def removeVowel(sentance):
    txt=""
    for i in range(len(sentance)):
        ch=sentance[i]
        ch=ch.lower()
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            continue
        else:
            txt=txt+ch
    return txt 

st=input("Enter a sentance: ")
print("Inputed String Without Vowel is: ",removeVowel(st))
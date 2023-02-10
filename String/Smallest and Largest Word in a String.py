def words(txt):
    if txt.strip()=="":
        return 0

    words=txt.split()

    max=len(words[0])                       #wrong answer
    min=len(words[0])
    for i in range(len(words)):
        if len(words[i])>max:
            max=len(words[i])
        if len(words[i])<min:
            min=len(words[i])
    return words[max],words[min]

string=input("Enter a String: ")
max,min=words(string)
print(f"Largest Word is:{max} || Smallest word is:{min}")
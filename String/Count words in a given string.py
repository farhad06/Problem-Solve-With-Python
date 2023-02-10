def count(string):
    if string.strip()=='':
        return 0 
    words=string.split()
    return len(words)  


st=input("Enter a String: ")
print("Number of words in this sentance is:",count(st))        
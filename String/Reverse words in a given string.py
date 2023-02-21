def reverseWord(string):
    words=string.split()
    rev_str=""
    for word in words[::-1]:
        # print(word)
        # rev_str=rev_str+" "+word
        rev_str="".join(word)
    return rev_str 

strn=input("Enter a string: ")
print("The reversed words string is:",reverseWord(strn))
txt=input("Enter a string ")
rev_txt=reversed(txt)
if(list(txt) == list(rev_txt)):
    print("The String is Palindrome")
else:
    print("The String is not Palindrome")    
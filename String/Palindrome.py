def isPalindrome(txt):
    sen=""
    for i in txt:
        sen=i+sen 
    return sen 

txt=input("Enter a string. ") 
if txt==isPalindrome(txt):
    print("String is Palindrome. ")
else:
    print("String is not palindrome.")           
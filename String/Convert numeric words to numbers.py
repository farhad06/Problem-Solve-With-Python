def convertToWord(txt):
    word_to_num={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    txt=txt.lower()
    words=txt.split()
    nums=[]
    for i in words:
        nums.append(word_to_num[i])
        res=''.join(nums)
    return res 

string=input("Enter a String: ")
print("Numeric form is:",convertToWord(string))
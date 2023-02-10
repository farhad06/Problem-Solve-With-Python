def split(txt):
    # txt=txt.lower()
    vowel='aeiouAEIOU'
    result=[]
    temp=""
    for i in txt:
        if i in vowel:
            if temp !='':
                result.append(temp)
                temp=""
        else:
            temp+=i
    if temp !="":
        result.append(temp)                
    return result        

st='GFGaBstuforigeeks' 
print(split(st))
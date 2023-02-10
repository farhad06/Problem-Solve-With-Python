from datetime import datetime
x=datetime.now()
print(x)

file_name=x.strftime('%d-%m-%Y.txt')
with open(file_name,'w') as f:
    f.write("This is a line")
    print("Created ",file_name)


file_name2=x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name2,'w') as f1:
    print("Created ",file_name2)  

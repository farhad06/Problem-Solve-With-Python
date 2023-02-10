l=int(input("Enter the Low value. "))
r=int(input("Enter the Upper Value. "))

s=0 
for i in range(l,r+1):
    s=s+i 
print(f"Sum between {l} and {r} is: {s}")    
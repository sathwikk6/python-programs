s=input("Enter the string: ")
str="" 
str=str.upper()
for i in str:
    if (i>='A' and i<='Z' or i>='a' and i<='z'):
        str += i
    elif (i>='0' and i<='9'):
        str += i
if str==str[::-1]:
    print(True)
else:
    print(False)

str=input("enter any string ")
a,d,s,spl=0,0,0,0
alpha=[]
digit=[]
spl_char=[]
for i in range(len(str)):
    if(str[i].isalpha()):
        a=a+1
        alpha.append(str[i])
    elif(str[i].isdigit()):
        d=d+1
        digit.append(str[i])
    else:
        spl=spl+1
        spl_char.append(str[i])
print("number of special characters are",spl_char,spl)
        

str=("saveetha school opf engineering")
v,c,s=0,0,0
vow=[]
conso=[]
space=[]
for i in range(len(str)):
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'
       or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):
        v=v+1
        vow.append(str[i])
    elif(str[i]==' '):
        s=s+1
        space.append(str[i])
    else:
        c=c+1
        conso.append(str[i])
print("total number of vowels and consonents are ")
print(v,vow)
print(c,conso)



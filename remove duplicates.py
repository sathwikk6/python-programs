l=[15,14,25,14,22,32,14]
x=[]
for i in l:
    if l.count(i)==1:
        x.append(i)
print(sorted(x))        

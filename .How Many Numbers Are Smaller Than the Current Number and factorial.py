def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*fact(n-1))
    

l=[8,1,2,2,3]
l1=[]
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]>l[j]:
            count+=1
    l1.append(count)
print(l1)
for k in range(len(l1)):
    print(fact(l1[k]),end=" ")

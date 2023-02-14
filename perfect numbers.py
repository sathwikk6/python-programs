n=int(input("enter"))
m=int(input("enter"))
a=[]
for i in range(n,m):
    b=(i*i)
    c=b%10
    d=b/10
    e=c+d
    if(b<=m and e<10):
        a.append(b)
    else:
        continue

    print(b)

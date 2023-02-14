l=[]
a=[]
b=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)
for i in l:
    if(i%2==0):
        a.append(i)
    else:
        b.append(i)
l1=[]
odd_squ=[sum(x**2 for x in b)]
l1.append(odd_squ)
even_squ=[sum(x**2 for x in a)]
l1.append(even_squ)
print(l1)

x=[0,0,0,0,0]
E=[7,0,5,1,3]
L=[1,2,1,3,4]
T=int(input("T="))
for i in range(0,T):
        x[i]=(x[i-1]+E[i])-L[i]
print(max(x))
    

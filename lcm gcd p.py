def gcd(a,b):
    gcd=1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            gcd=i
    return i
a=int(input("enter any number"))
b=int(input("enter any number"))
print("gcd is",gcd(a,b))
lcm=a*b/gcd(a,b)
print("lcm is",lcm)

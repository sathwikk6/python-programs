def find_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print("gcd is",find_gcd(a,b))
lcm = a * b/ find_gcd(a,b)
print("lcm is",lcm)

L1=[16,18,27,16,23,21,19]
prime=[]
composite=[]
for num in L1:
    if num==2:
        prime.append(num)
    else:
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                composite.append(num)
                break
        if is_prime:
            prime.append(num)
print("composite are",composite,len(composite))

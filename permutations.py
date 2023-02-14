from itertools import permutations
a=permutations([1,1,2])
b=[]
for i in a:
    b.append(i)
print(list(set(b)))

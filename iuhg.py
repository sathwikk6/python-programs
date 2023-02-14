text=input("enter any string")
vowels=['a','e','i','o','u','A','E','I','O','U']
newtext=""
for i in range(len(text)):
    if text[i] not in vowels:
        newtext=newtext+text[i]
print("\nstring after removing vowels is")
text=newtext
print(text)

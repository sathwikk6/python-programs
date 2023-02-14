string= "saveetha school of engineering"
print(string)
rep_word={}
for i in string:
    if i in rep_word:
        rep_word[i]=rep_word[i]+1
    else:
        rep_word[i] = 1
result= max(rep_word, key = rep_word.get)
print("Most frequent character: ",result)

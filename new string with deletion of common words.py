def UncommonWords(A, B):
    sent1=list(A.split())
    sent2=list(B.split())
    common=[]
    for i in sent1:
        if i in sent2:
            sent1.remove(i)
            sent2.remove(i)
            common.append(i)
    print(*sent1)
    print(*sent2)
    print("Common words: ",common)

A = "sky is blue in colour"
B = "raj like sky blue colour"
UncommonWords(A, B)

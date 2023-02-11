#Given two strings “s” and “t”, determine if they are isomorphic
#Two strings “s” and “t” are isomorphic if the characters in “s” can be
#replaced to get “t”. All occurrences of a character must be replaced with
#another character while preserving the order of characters. No two
#characters may map to the same character, but a character may map toitself. 

def isisomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        map1, map2 = {}, {}
        for i in range(len(str1)):
            ch1, ch2 = str1[i], str2[i]
            if ch1 not in map1:
                map1[ch1] = ch2
            if ch2 not in map2:
                map2[ch2] = ch1
            if map1[ch1] != ch2 or map2[ch2] != ch1:
                return False
    return True


str1 = input("String 1=")
str2 = input("String 2=")
print(isisomorphic(str1, str2))

Output: 
String 1=egg
String 2=add
True

#Modify string by replacing characters by alphabets whose distance from that character is equal to its frequency. Given a string S consisting of N lowercase alphabets, the task is to modify the string S by replacing each character with the alphabet whose circular distance from the character is equal to the frequency of the character in S.
Sol:
def addFrequencyToCharacter(s):
     
    # Stores frequency of characters
    frequency = [0] * 26
 
    # Stores length of the string
    n = len(s)
 
    # Traverse the given string S
    for i in range(n):
         
        # Increment frequency of
        # current character by 1
        frequency[ord(s[i]) - ord('a')] += 1
 
    # Traverse the string
    for i in range(n):
         
        # Store the value to be added
        # to the current character
        add = frequency[ord(s[i]) - ord('a')] % 26
 
        # Check if after adding the
        # frequency, the character is
        # less than 'z' or not
        if (ord(s[i]) + add <= ord('z')):
            s[i] = chr(ord(s[i]) + add)
 
        # Otherwise, update the value of
        # add so that s[i] doesn't exceed 'z'
        else:
            add = (ord(s[i]) + add) - (ord('z'))
            s[i] = chr(ord('a') + add - 1)
 
    # Print the modified string
    print("".join(s))
 
# Driver Code
if __name__ == '__main__':
     
    str = input("Enter the string: ")
     
    addFrequencyToCharacter([i for i in str])

#Output:
#Enter the string: ghee
#higg


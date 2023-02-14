string = "Welcome to TutorialsPoint family";
print("All the duplicate characters in the string are: "); 
for s in range(0, len(string)): 
   count = 1; 
   for t in range(s+1, len(string)):
      if(string[s] == string[t] and string[s] != ' '): 
         count = count + 1;  
   string = string[:t] + '0' + string[t+1:];  
   if(count > 1 and string[s] != '0'): 
      print(string[s]," - ",count);

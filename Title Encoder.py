f=open("/usercode/files/books.txt", "r")
first_chars = []
for line in f:
    first_chars.append([word[0] for word in line.split()])

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += str(ele)   
    
    # return string   
    return str(str1)  
i=0

while i < len(first_chars):                
    print(listToString(first_chars[i]))
    i+=1
f.close()
#finding count of each alphabet, print in alphabetical order
a='geeksforgeeks'

def freq(a):
    hash_count={}
    for i in range(1,27):
        hash_count[i]=0
    for i in a:
        hash_count[ord(i)-96]+=1
    for i in hash_count.keys():
        if hash_count[i]!=0:
            print(chr(96+i),'=>',hash_count[i])
            
freq(a)    
    

#anagram check
a='abcbaddf'
b='abcbaddg'
def is_anagram(a,b):
    if len(a)!=len(b):
        print(False)
        return
    hasha={}
    hashb={}
    for i in a:
        if i not in hasha:
            hasha[i]=1
        else:
            hasha[i]+=1
    for i in b:
        if i not in hashb:
            hashb[i]=1
        else:
            hashb[i]+=1
    for j in hasha.keys():
        try:
            if hasha[j]!=hashb[j]:
                print(False)
                return
        except:
            print(False)
            return
    print(True)
    
    
is_anagram(a,b)    
        
    
        

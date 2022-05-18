def pat_ser(s,sub):
    if len(s)<len(sub):
        return -1
    
    start=0
    end=len(sub)
    while(end<len(s)):
        #PRINT(s[start:end])
        if s[start:end]==sub:
            print (start,end=' ')
        start+=1
        end+=1
    return 

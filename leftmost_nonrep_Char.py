#leftmost non rep char
def lnonrep(s):
    n=len(s)
    h={}
    for i in range(n):
        if s[i] in h:
            h[s[i]]=-1
        else:
            h[s[i]]=i
    for i in h.keys():
        if h[i] !=-1:
            print(h[i])
            return
    print (-1)
lnonrep('appale')
    

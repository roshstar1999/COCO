#Pallindrome check
a='ABBAG'
def pal_check(a):
    flag=0
    for i in range(0,len(a)//2-1):
        if a[i]!=a[len(a)-1-i]:
            flag=1
            break
    if flag==0:
        print('string is pallindrome')
    else:
        print('string is not a pallindrome')
        
pal_check(a)
    

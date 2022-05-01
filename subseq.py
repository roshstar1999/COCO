#string is subsequence or not
a='ABBAG'
sub='AAG'
def is_subseq(a,sub):
    si=0
    ssi=0
    n=len(a)
    m=len(sub)
    while ssi!=m:
        if si==len(a):
            print('not subsequence')
            return
            
        if a[si]==sub[ssi]:
            ssi+=1
        si+=1
    print('yes, a subsequence')
is_subseq(a,sub)      

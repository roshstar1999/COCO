a=[[1,2,3,4,5],[12,77,88,99,6],[11,10,9,8,7]]

def boundary_traversal(a):
    r=len(a)
    c=len(a[0])
    i,j=0,1

    if r==1:
        print(a)
    if c==1:
        print(a)
    else:

        print(a[0][0], end=" ")

        while(i!=0 or j!=0):
            print(a[i][j], end=" ")

            if i==0 and j<c-1:
                j+=1
            elif i<r-1 and j== c-1:
                i+=1
            elif i==r-1 and j>0:
                j-=1
            elif i>0 and j==0:
                i-=1
    
    return('')
print(boundary_traversal(a))

def rotate_90(a,n):
    i=0
    j=0
    while i<n and j<n:
        if i!=j:
            a[i][j],a[j][i]=a[j][i],a[i][j]

        if j==n-1:
            i+=1
            j=i
        else:
            j+=1
    for i in range(0,n):
        for j in range(0,n//2):
            a[i][j],a[i][n-j-1]=a[i][n-j-1],a[i][j]
        
    
        
        
        
    
        
       
    print(a)

a=[[1,2,3],[4,5,6],[7,8,9]]
n=len(a[0])
rotate_90(a,n)


                

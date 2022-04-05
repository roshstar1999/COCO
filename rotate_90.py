def rotate_90(a,n):
    new=[[0]*3]*3
    print(new)
    for i in range(0,n):
        j=0
        for j in range(0,n):
            new[n-j-1][i]=a[i][j]
            print(n-j-1,i," " ,new[n-j-1][i],a[i][j])
    print (new)    
    for i in range(0,n):
        for j in range(0,n):
            a[i][j]=new[i][j]
    print(a)

a=[[1,4,7],[2,5,8],[3,6,9]]
rotate_90(a,3)

def matrix_transp(a,n):
    i=0
    j=0
    while i!=n:
        if i!=j:
            temp=a[i][j]
            a[i][j]=a[j][i]
            a[j][i]=temp
        if j<n-1:
            j+=1
        else:
            
            i+=1
            j=i
    print(a)
            
a=[[1,4,7],[2,5,8],[3,6,9]]
matrix_transp(a,3)

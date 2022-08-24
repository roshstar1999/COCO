 n=len(matrix)
        setr=set()
        setc=set()
        for i in range(n):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    setr.add(i)
                    setc.add(j)
        for i in range(n):
            for j in range(len(matrix[0])):
                if i in setr or j in setc:
                    matrix[i][j]=0
        
                    

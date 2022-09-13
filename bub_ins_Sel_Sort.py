def selsort(arr):
    
    n=len(arr)
    
    for i in range(0,n-1):
        min=i
        
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
                
        arr[min],arr[i]=arr[i],arr[min]
    return arr
        
arr=[5,4,3,-1,5,2,1]


def bubsort(arr):
    n=len(arr)
    for i in range(n-1):
        
        for j in range(n-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr
'''  
def ins_sort(arr):
    n=len(arr)
    arr2=[arr[0]]
    
    for i in range(1,n):
        j=0
        for j in range(len(arr2)):
            if arr[i]<=arr2[j]:
                arr2.insert(j,arr[i])
                break
        if arr[i]>arr2[j]:
            arr2.append(arr[i])
    print(arr2)
'''    
def ins_sort(arr):
    
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<=arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    
    return arr
            
    
    
print(ins_sort2(arr))
    
                
            
print(bubsort(arr))

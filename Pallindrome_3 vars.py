def isPalindrome(self, n : int ) -> bool:
        
        #number 1-> by reversing the number in integer and checking
        x=n
        a=0
        while x!=0:
            a=a*10+x%10
            x//=10
        return a==n
      
        #number 2->checking by converting into the string and checking last elements from r and l till middle .
        x=len(str(n))
        for i in range(x//2):
            if (str(n))[i]!=(str(n))[x-i-1] :
                return False
        return True
    
       #number 3 ->str reverse compare using indexing slicing for efficiency MOST EFFECIENT HERE
        if n!=0 or len(n)!=1:
            return str(n) == str(n)[::-1]
        return True
        

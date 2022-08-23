 
        f=s=dummy=ListNode(0)
        
        f.next=s.next=head
        
        for i in range (n+1):
            f=f.next
        
        while f:
            f=f.next
            s=s.next
        s.next = s.next.next
        
        return dummy.next
                

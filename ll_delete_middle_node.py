 def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        tmp=head
        count=0
        while tmp:
            count+=1
            tmp=tmp.next
            
        n=count//2-1
        
        tmp=head
        for i in range(n):
            tmp=tmp.next
        if tmp.next:
            tmp.next=tmp.next.next
        else:
            tmp.next=None
        return head
        

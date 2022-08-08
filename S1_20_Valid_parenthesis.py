class Solution:
    def isValid(self, s: str) -> bool:
        class Node:
            def __init__(self,val=None):
                self.val=val
                self.next=None
        class LL:
            def __init__(self):
                self.head=None
            
                
        class Stack:
            def __init__(self):
                self.LL=LL()
            def isEmpty(self):
                if self.LL.head==None:
                    return True
            def peek(self):
                if self.LL.head==None:
                    return 'Empty Stack'
                else:
                    return self.LL.head.val
            def push_(self,val):
                newNode=Node(val)
                newNode.next=self.LL.head
                self.LL.head=newNode
            def pop_(self):
                if self.LL.head==None:
                    return 'Empty'
                else:
                    newNode=self.LL.head
                    self.LL.head=self.LL.head.next
                    return (newNode.val)
                    
                
                
        S=Stack()
        d={'(':')','[':']','{':'}'}
        for i in s:
            if i in d.keys():
                S.push_(i)
            else:
                
                if S.isEmpty() or i != d[S.peek()]:
                    return False
                else:
                    S.pop_()
        if S.isEmpty():
            return True
        else:
            return False
                    
                
        

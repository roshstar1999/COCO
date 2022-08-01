# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:c
        print("Hello World")

class Node:
  
class LL:
  
  def Intersect(ll1,ll2):
    h1=ll1.head
    h2=ll2.head
    
    #calculate length of the lls
    l1=0
    l2=0
    curr=h1
    while curr:
      l1+=1
      curr=curr.next
    curr=h2
    while curr:
      l2+=1
      curr=curr.next
    
    #if lengths are different, we have to ignore extra nodes by changinng the starting point
    #for the check.
    if l1!=l2:
      dif=abs(l1-l2)
      if l1>l2:
        
        while(dif):
          h1=h1.next
          dif-=1
      else:
        
        while(dif):
          h2=h2.next
          dif-=1
    
    while h1 and h2:
      if h1==h2:
        return True
      h1=h1.next
      h2=h2.next
    
    return False
    
    
        
        

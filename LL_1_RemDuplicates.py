#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.val = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        curNode=head
        dic={}
        while curNode:
            if curNode.data not in dic:
                dic[curNode.data]=0
                prevNode=curNode
                curNode=curNode.next
                
                
            else:
                prevNode.next = curNode.next
                curNode = prevNode.next
        return head
                
                
        # return head after editing list


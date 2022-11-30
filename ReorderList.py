#User function Template for python3

#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        
        if (head==None or head.next==None):
            return
        
        n=0
        walk=head
        
        while(walk):
            walk=walk.next
            n=n+1
        head2=head
        
        for i in range((n-1)//2):
            head2=head2.next
            
        tail=head2
        head2=head2.next
        tail.next=None
        prv=None
        nex=head2.next
        
        while(head2):
            nex=head2.next
            head2.next=prv
            prv=head2
            head2=nex
            
        head2=prv
        walk=head
        walk2=head2
        
        while(walk2):
            temp=walk.next
            walk.next=walk2
            walk=temp
            temp=walk2.next
            walk2.next=walk
            walk2=temp
            
        if( tail.next ):
            tail=tail.next
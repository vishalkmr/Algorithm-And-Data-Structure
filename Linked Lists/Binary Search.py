'''
    Binary Search of the given element in linked-list
    Assume that linked-list is already in Ascending order.
'''

from LinkedList import Node


def binary_search(head,data):
    """
    Retruns True if given data is present in linked-list
    Syntax: binary_search(head,data) 
    Time Complexity: O(n)
    Recurence Relation : T(n)=T(n/2)+n  
    """
    #if only one element in the linked-list (Terminating Condition)
    if head.next==None:
        if head.data==data:
            return True
        else:
            return False

    mid=middle(head)   #calculating middle node
    
    right_list=mid.next #right list contains nodes from mid+1 upto last node
    mid.next=None #breaking the original list into two portion from mid
    left_list=head #left list contains nodes from head to mid node

    if data == mid.data:
        return True
    
    elif mid.data<data:
        return binary_search(right_list,data)
    
    elif mid.data>data:
        return binary_search(left_list,data)


def middle(head):
    """
    Returns middle element of linked-list
    Syntax: middle(head) 
    Time Complexity: O(n)           
    """
    slow = fast =head
    while fast and fast.next and fast.next.next:
        slow=slow.next #slow takes one step at a time
        fast= fast.next.next #fast takes two step at a time	

    return slow    
            
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=None

result=binary_search(a,5)
print(result)
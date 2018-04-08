'''
    Linear Search of the given element in linked-list
'''

from LinkedList import Node


def linear_search(head,data):
    """
    Retruns True if given data is present in linked-list
    Syntax: linear_search(head,data) 
    Time Complexity: O(n)
    """
    current =head
    
    while current :
        if current.data == data:
            return True
        current = current.next

    return False    



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


result=linear_search(a,4)
print(result)
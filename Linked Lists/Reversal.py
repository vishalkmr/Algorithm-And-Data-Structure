'''
 Reverse the elements of linked-list
 
 Example :
 linked-list 1,2,3,4,5,6
 after reversal becomes 6,5,4,3,2,1
'''

from LinkedList import LinkedList


def reversal(linked_list):
    """
    Function to reverse the elements of linked-list
    Syntax: reversal() 
    Time Complexity: O(n)         
    """              

    previous=linked_list.head
    current=linked_list.head        
    ahead=current.next
    linked_list.head.next=None #1st element become last element
    
    while ahead:
        current=ahead
        ahead=ahead.next
        current.next=previous
        previous=current

    linked_list.head=current # now head points to last element 



linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)

print(linked_list)
result=reversal(linked_list)
print(linked_list)


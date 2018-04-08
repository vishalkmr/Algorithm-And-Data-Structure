'''
    Check the given limked-list is cyclic or not
'''

from LinkedList import LinkedList


#using Set
def is_cyclic(linked_list):
    """
    Returns True if linked-list is cyclic
    Syntax: is_cyclic(linked_list) 
    Time Complexity: O(n)           
    """
    # if linked-list is empty
    if not linked_list.head or not linked_list.head.next:
        return False

    visited=set()
    current=linked_list.head

    while  current:
        #if the node is already in visited set that mean linked-list is cyclic
        if current.data in visited:
            return True
        #if the node is not visited set that means it appears 1st time so add it on the visited set
        else:
            visited.add(current.data)
        #incement the loop counter    
        current=current.next           

    return False    



def is_cyclic(linked_list):
    """
    Returns True if linked-list is cyclic
    Syntax: is_cyclic(linked_list) 
    Time Complexity: O(n)           
    """
    # if linked-list is empty
    if not linked_list.head or not linked_list.head.next:
        return False

    slow = fast =linked_list.head
    
    while fast and fast.next:
        slow=slow.next #slow takes one step at a time
        fast= fast.next.next #fast takes two step at a time
        
        #if slow meets with fast that means linked-list is cyclic
        if fast==slow:
            return True
    return False    


linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)

#making the linked-list cyclic
linked_list.tail.next=linked_list.head


result=is_cyclic(linked_list)
print(result)


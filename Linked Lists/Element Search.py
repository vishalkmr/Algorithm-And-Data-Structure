'''
    Search the given element in linked-list
'''

from LinkedList import LinkedList


def search(linked_list,data):
    """
    Retruns True if given data is present in linked-list
    Syntax: search(linked_list,data) 
    Time Complexity: O(n)
    """
    current =linked_list.head
    
    while current :
        if current.data == data:
            return True
        current = current.next

    return False    



linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)


result=search(linked_list,3)
print(result)
'''
 Swap every two adjacent nodes of linked-list
  
 Example:
 link-list : 1,2,3,4,5,6
 after pairwise swap linked-list becomes 2,1,4,3,6,5
'''

from LinkedList import LinkedList


def swap_pairs(linked_list):
    """
    Swap every two adjacent nodes of linked-list 
    Syntax: swap_pairs(linked_list) 
    Time Complexity: O(n)           
    """
    
    # if linked-list is empty or it contains single element
    if linked_list.size==0 or linked_list.size==1:
        return
    current=linked_list.head
    previous=None
    while current and current.next:            
        previous=current
        current=current.next
        previous.data,current.data=current.data,previous.data #swaping data
        previous,current=current,current.next #jumping to next pair



linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)

print(linked_list)
result=swap_pairs(linked_list)
print(linked_list)


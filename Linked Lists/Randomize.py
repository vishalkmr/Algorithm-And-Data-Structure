'''
    Randomize the given Linked-List
'''

from LinkedList import LinkedList
import random

def randomize(linked_list):
    """
    Randomize elements of linked-list 
    Syntax: randomize() 
    Time Complexity: O(n^2)     
    Space Complixity: O(n)      
    """
    
    # if linked-list is empty or it contains single element
    if linked_list.size==0 or linked_list.size==1:
        return
    size= linked_list.size   
    random_list=LinkedList()
    
    while True:
        current=linked_list.head
        r=random.randint(0,linked_list.size) 
        
        #if only 1 element is present in linked_list the add it to random_linked_list and delete it from linked_list
        if linked_list.size==1:
            random_list.insert_end(current.data)
            linked_list.delete(current.data) 
        
        #otherwise
        else:  
            #choosing a random postion and the insert that position element into random_linked_list and delete it from linked_list         
            while  r and current:        
                current=current.next
                r=r-1
            if current and r==0:
                random_list.insert_end(current.data)
                linked_list.delete(current.data)  
               
        if len(random_list)==size:
            break  
    
    linked_list.head=random_list.head
    linked_list.size=random_list.size

linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)


print(linked_list)
randomize(linked_list)
print(linked_list)


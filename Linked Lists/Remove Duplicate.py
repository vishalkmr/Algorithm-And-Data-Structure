'''
 Remove Duplicate items from the linked-list 

 Example :
 linked-list 1,2,3,4,5,6,3,1,4
 after removing the duplicates the list becomes 1,2,3,4,5,6
'''

from LinkedList import LinkedList

#using Set
def remove_duplicate(linked_list):
    """
    Function to remove duplicate items from the linked-list
    Syntax: remove_duplicate(linked_list) 
    Time Complexity: O(n) 
    Space Complexity: O(n)          
    """    
    unique_item_set=set()
    current =linked_list.head
    previous=None

    while current :
        #if the node is already present in unique_item_set
        #means repeatation of that node take place 
        if current.data  in unique_item_set:
            #if the repeated item is last element then update the tail 
            if current is linked_list.tail:
                linked_list.tail=previous
            
            previous.next=current.next #skiping that repeated node
            linked_list.size-=1
        
        #otherwise
        else:
            #node is appears 1st time hence add it to unique_item_set
            unique_item_set.add(current.data)
            previous=current

        #incrementing loop counter    
        current=current.next



linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)
linked_list.insert_end(3)
linked_list.insert_end(1)
linked_list.insert_end(4)


print(linked_list)
remove_duplicate(linked_list)
print(linked_list)
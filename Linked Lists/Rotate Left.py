'''
 Rotates the linked-list by k in left side
 
 Example:
 link-list : 1,2,3,4,5,6
 after 2 rotation to left it becomes 3,4,5,6,1,2
'''

from LinkedList import LinkedList


def rotate_left(linked_list,k):
    """
    Rotates the linked-list by k in left side
    Syntax: rotate_left(k) 
    Time Complexity: O(n)        
    """
    #for circular rotation
    if k>=len(linked_list):
        k=k%len(linked_list)
    
    if len(linked_list)==0 or k==0:
        return
  
    count=0
    current=linked_list.head
    previous=None
    
    #break the linked_list into two portion (head node to (k-1)th node) and (kth node to last node) 
    while current and count!=k:
        previous=current
        current=current.next
        count=count+1
    
    previous.next=None

    #previous represent new likedlist last element
    linked_list.tail=previous #update the new linked_list tail

    #now list is splited into two portion
    #1st contains node form begining of original linked_list to previous node (left list)
    #2nd contains from current node to last node (right list)
    
    #for rotation we just have to append 1st linked-list after 2nd linked-list
    if  count==k:
        ptr=current
        while ptr.next:
            ptr=ptr.next

        #ptr points to 2nd linked_list last node    
        #joining the 1st linked_list at the end of 2nd linked_list 
        ptr.next=linked_list.head         
        
        linked_list.head=current #update the new linked_list head



linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
linked_list.insert_end(6)

print(linked_list)
result=rotate_left(linked_list,2)
print(linked_list)


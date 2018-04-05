'''
 Find the intersection between two linked-list
'''

from LinkedList import LinkedList


def intersection(first_linked_list,second_linked_list):
    """
    Returns the node where the first_linked_list intercept with second_linked_list
    Syntax: intersection(first_linked_list,second_linked_list)
    Time Complexity: O(n)           
    """
    #if first_linked_list is large
    if first_linked_list.size > second_linked_list.size:
        difference=first_linked_list.size - second_linked_list.size
        current1=first_linked_list.head
        
        while current1 and difference:            
            current1=current1.next    
            difference=difference-1   
        
        current2=second_linked_list.head
     
        while current1 and current2:                
            if current1 == current2:
                return current1.data
            current1=current1.next
            current2=current2.next    
        return False                                          
   
    #if second_linked_list is large
    else:
        difference=second_linked_list.size - first_linked_list.size            
        current1=second_linked_list.head
        
        while current1 and difference:            
            current1=current1.next    
            difference=difference-1       
        
        current2=first_linked_list.head
        
        while current1 and current2:               
            if current1 == current2:                    
                return current1.data
            current1=current1.next
            current2=current2.next                
        return False  
   


first_linked_list=LinkedList()
first_linked_list.insert_end('F1')
first_linked_list.insert_end('F2')
first_linked_list.insert_end('F3')
first_linked_list.insert_end('F4')
first_linked_list.insert_end('F5')
first_linked_list.insert_end('F6')

second_linked_list=LinkedList()
second_linked_list.insert_end('S1')
second_linked_list.insert_end('S2')
second_linked_list.insert_end('S3')


#making them intersect
second_linked_list.tail.next=first_linked_list.head
second_linked_list.size =second_linked_list.size+first_linked_list.size 

print(first_linked_list )
print(second_linked_list )

result=intersection(first_linked_list,second_linked_list)
print(result)


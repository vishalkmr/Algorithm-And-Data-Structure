'''
 Merg two sorted linked-list into one linked-list
 Assume that both the given linked-list are in Ascending order
 Example :
 list-1 contains 1,3,6,7,9
 list-2 contains 2,4,8,10
 meged list : 1,2,3,4,6,7,8,9,10S
'''

from LinkedList import LinkedList


def merg(first_linked_list,second_linked_list):
    """
    Returns the merged list formed from merging first_linked_list and second_linked_list
    Syntax: merg(first_linked_list,second_linked_list)
    Time Complexity: O(m+n)           
    """
    first=first_linked_list.head
    second=second_linked_list.head
    output=LinkedList() #contains the merged linked-list

    while first and second:
    	if second.data<first.data:
    		output.insert_end(second.data)
    		second=second.next
    	else:
    		output.insert_end(first.data)
    		first=first.next

    
    while first:
    		output.insert_end(first.data)
    		first=first.next

    while second:
    		output.insert_end(second.data)
    		second=second.next

    return output		

first_linked_list=LinkedList()
first_linked_list.insert_end(1)
first_linked_list.insert_end(3)
first_linked_list.insert_end(5)
first_linked_list.insert_end(9)
first_linked_list.insert_end(15)
first_linked_list.insert_end(30)

second_linked_list=LinkedList()
second_linked_list.insert_end(4)
second_linked_list.insert_end(12)
second_linked_list.insert_end(20)


print(first_linked_list )
print(second_linked_list )

output=merg(first_linked_list,second_linked_list)

print(output)

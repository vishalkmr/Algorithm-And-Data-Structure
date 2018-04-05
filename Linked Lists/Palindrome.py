'''
    Check that given linked-list is Palindreome or not
'''

from LinkedList import LinkedList


def is_palindrome(linked_list):
    """
    Returns True if linked-list is palindrome
    Syntax: is_palindrome() 
    Time Complexity: O(n)           
    """
    # if linked-list is empty
    if not linked_list.head or not linked_list.head.next:
        return True
    
    # Get the midpoint 
    slow = fast = current = linked_list.head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # Push the second half into the stack
    stack = [slow.data]
    while slow.next:
        slow = slow.next
        stack.append(slow.data)

    # Comparison
    while stack:
        if stack.pop() != current.data:
            return False
        current = current.next

    return True



linked_list=LinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(3)
linked_list.insert_end(2)
linked_list.insert_end(1)


result=is_palindrome(linked_list)
print(result)




from Stack import Stack

def towers_of_hanoi(size,left_stack,middle_stack,rigth_stack):
    ''' 
    Funtion to reverse string
    Syntax: towers_of_hanoi(size,left_stack,middle_stack,rigth_stack)
    Time Complexity: O(2^n)  	
    '''	
    if size==0:
        return
    #moving all the content of left_stack except its bottom element to middle_stack with the help right_stack    
    towers_of_hanoi(size-1,left_stack,rigth_stack,middle_stack) 
    
    #now move the remaining bottom element of left_stack to the right_stack
    move(left_stack,rigth_stack)
    
    #moving the the content of updated middle_stack to right_stack with the help left_stack
    towers_of_hanoi(size-1,middle_stack,left_stack,rigth_stack) 


#funtion to move top element from source to destination
def move(source,destination):
    destination.push(source.pop())




left_stack=Stack()
rigth_stack=Stack()
middle_stack=Stack()

left_stack.push('OOO')
left_stack.push('OO')
left_stack.push('O')


towers_of_hanoi(len(left_stack),left_stack,middle_stack,rigth_stack)

print('\t\tRight Stack Becames')
rigth_stack.display()
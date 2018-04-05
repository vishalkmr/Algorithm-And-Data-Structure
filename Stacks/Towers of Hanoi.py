'''
The Tower of Hanoi is a mathematical game or puzzle. 
It consists of three rods(Stacks) and a number of disks of different sizes (elements with different values) , 
which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod , 
the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1.Only one disk can be moved at a time.
2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3.No disk may be placed on top of a smaller disk.
''' 

from Stack import Stack

def towers_of_hanoi(size,left_stack,middle_stack,right_stack):
    ''' 
    Funtion to reverse string
    Syntax: towers_of_hanoi(size,left_stack,middle_stack,right_stack)
    Time Complexity: O(2^n)
    Recurence Relation : T(n)=2T(n-1)+C  (C represents constant)  	
    '''	
    if size==0:
        return
    #moving all the content of left_stack except its bottom element to middle_stack with the help right_stack    
    towers_of_hanoi(size-1,left_stack,right_stack,middle_stack) 
    
    #now move the remaining bottom element of left_stack to the right_stack
    right_stack.push(left_stack.pop())
    
    #moving the the content of updated middle_stack to right_stack with the help left_stack
    towers_of_hanoi(size-1,middle_stack,left_stack,right_stack) 


left_stack=Stack()
right_stack=Stack()
middle_stack=Stack()

left_stack.push('OOO')
left_stack.push('OO')
left_stack.push('O')


towers_of_hanoi(len(left_stack),left_stack,middle_stack,right_stack)


print('\t\tRight Stack Becames')
right_stack.display()
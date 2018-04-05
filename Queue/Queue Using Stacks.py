'''
 Reverse the given string using Stack

'''

class Queue:
    """Class to implement Queue Data Structure using 2 Stacks"""
    def __init__(self):
        """
        constructing a queue 
        """
        self.input_stack=Stack() #for enqueue purpose
        self.output_stack=Stack() #for dequeue purpose
        self.length=0

    def size(self):
        """ 
        return the size of queue 
        Syntax: size()  
        Time Complexity: O(1)  
        """   
        return self.length

    def peek(self):
        """
        function to return the front element value
        Syntax: peek()  
        Time Complexity: O(n)  
        """
        if self.is_empty():
            raise IndexError("Front element doesnot exixts Because Queue is empty")
        
        if self.output_stack.is_empty():
            while(not self.input_stack.is_empty()):
                self.output_stack.push(self.input_stack.pop())

        return self.output_stack.peek()

    def is_empty(self):
        """ 
        return the true if queue is empty
        Syntax: is_empty()  
        Time Complexity: O(1)   
        """   
        return self.length==0
   

    def enqueue(self,item):
        """ 
        function to insert a given element on rear end of queue
        Syntax: enqueue(item)  
        Time Complexity: O(1)  
        """
        #adding element at rear end
        #input_stack top represents rear end of queue
        #so push the item onto input_stack to enqueue item in the queue
        self.input_stack.push(item)
        self.length+=1 #Increment the queue length


    def dequeue(self):
        """ 
        function to delete element from front end of queue
        Syntax: dequeue(item)  
        Time Complexity: O(n)          
        """        
        #if queue is empty
        if self.input_stack.is_empty() and self.output_stack.is_empty():
            raise IndexError("Deletion is not Possible Because Queue is Empty")
        #otherwise perform deletion
        else:
        	#deletion always take place from output_stack because output_stack top represent front end of queue
        	#if output_stack is empty then repeatedly pop the element from input_stack and push them into output_stack untile input_stack is empty
            if self.output_stack.is_empty():
                while(not self.input_stack.is_empty()):
                    self.output_stack.push(self.input_stack.pop())

            #finally pop the element from output_stack to delete the front elemnet of queue        
            item=self.output_stack.pop()
            self.length-=1 #Decrement the queue length
            return item




class Stack:
    """Class to implement Stack Data Structure using basic list operations"""

    def __init__(self):
        """
        constructing a stack 
        """
        self.items=[]
    
    def __str__(self):
        """
        for printing the stack elemetns
        """
        return self.display()   

    def __repr__(self):
        """
        for representaions of stack elemetns
        """
        return self.display()
 
    def __len__(self):
        """
        for length of stack object 
        """
        return self.size()         

    def __iter__(self):   
        """
        stack elements iterations from top to bottom
        """
        i = len(self.items) - 1
        while True:
            if i < 0:
                raise StopIteration
            yield self.items[i]
            i -= 1   

    def peek(self):
        """
        function to return the top element value
        Syntax: peek()
        Time Complexity: O(1)  
        """
        if self.is_empty():
            raise IndexError("Top element doesnot exixts Because Stack is empty")
        return self.items[-1]

    def size(self):
        """ 
        return the size of stack 
        Syntax: size()
        Time Complexity: O(1)     
        """   
        return len(self.items) 

    def is_empty(self):
        """ 
        return the true if stack is empty
        Syntax: is_empty()
        Time Complexity: O(1)      
        """   
        return self.items == []

    def display(self):
        """ 
        function to display the stack elements
        Syntax: display() 
        Time Complexity: O(1)     
        """ 
        # if stack is empty
        if(len(self.items)<=0):
            print("Stack is Empty",end='')
            return  str() #for representaion purpose
        #otherwise
        else:
            print('-'*11,'Stack','-'*11)
            print('Top : '+str(self.items[-1]))
            print('Elements : '+str(self.items))
            print('Size : '+str(len(self.items)))
            print('-'*30)
        return str() #for representaion purpose

    def push(self,item):
        """ 
        function to add a given element in at the top of the stack
        Syntax: push(item) 
        Time Complexity: O(1)             
        """
        self.items.append(item)
    
    def pop(self):
        """ 
        function to delete and return the top most element in stack
        Syntax: pop() 
        Time Complexity: O(1)             
        """
        # if stack is empty
        if self.is_empty():
            raise IndexError("Pop Operetion is not Possible Because Stack is Empty ")        
        # otherwise
        else:
            item=self.items[-1]
            del self.items[-1] # deleting top(last) element
            return item




if __name__ == '__main__':
    obj=Queue()
    while(1):
        print("\n------------")
        print("Queue Menu")
        print("1.Enqueue")
        print("2.Dequeue")
        print("3.Peek")
        print("4.Exit")
        print("------------")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            item=input("\nEnter the element you want to insert in queue : ")
            obj.enqueue(item)
        elif(choice==2):
            item=obj.dequeue()
            print("\nThe deleted element is : ",item)
        elif(choice==3):
            item=obj.peek()
            print("\nThe Front element is : ",item)  
        elif(choice==4):
            print("\nExiting ......")
            break
        else:
            continue
 
		

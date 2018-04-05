'''
 Implementation of Stack Data Structure using Queue
'''

class Stack:
    """Class to implement Stack Data Structure using 2 Queue"""

    def __init__(self):
        """
        constructing a stack 
        """
        self.input_queue=Queue()
        self.output_queue=Queue() 
        self.length=0
    

    def peek(self):
        """
        function to return the top element value
        Syntax: peek()
        Time Complexity: O(n)  
        """
        if self.is_empty():
            raise IndexError("Top element doesnot exixts Because Stack is empty")
        item=None
        while(len(self.input_queue)!=0):
            item=self.input_queue.dequeue()
            self.output_queue.enqueue(item)

        self.input_queue=self.output_queue
        self.output_queue=Queue()
        return item

    def size(self):
        """ 
        return the size of stack 
        Syntax: size()
        Time Complexity: O(1)     
        """   
        return self.length

    def is_empty(self):
        """ 
        return the true if stack is empty
        Syntax: is_empty()
        Time Complexity: O(1)      
        """   
        return self.length == 0


    def push(self,item):
        """ 
        function to add a given element in at the top of the stack
        Syntax: push(item) 
        Time Complexity: O(1)             
        """
        #queeue1 contains the pushed items
        self.input_queue.enqueue(item)
        self.length+=1  #increment the length of stack
    
    def pop(self):
        """ 
        function to delete and return the top most element in stack
        Syntax: pop() 
        Time Complexity: O(n)             
        """
        # if stack is empty
        if self.input_queue.is_empty() and self.output_queue.is_empty():
            raise IndexError("Pop Operetion is not Possible Because Stack is Empty ")        
        # otherwise perform pop 
        else:
            #last element of input_queue is top of stack
            #so delete the items from input_queue and insert them into output_queue until only 1 item is left which is top of stack
            while(len(self.input_queue)!=1):
                self.output_queue.enqueue(self.input_queue.dequeue())
            
            #item represent top of stack
            item=self.input_queue.dequeue()
            
            self.input_queue=self.output_queue #rename output_queue as input_queue which contains all element after deletion of top element of stack
            self.output_queue=Queue() #make the output_queue empty
            self.length-=1    #decrement the length of stack
            return item




class Queue:
    """Class to implement Queue Data Structure using basic list operations"""
    def __init__(self):
        """
        constructing a queue 
        """
        self.items=[]
    
    def __str__(self):
        """
        for printing the queue elemetns
        """
        return self.display()

    def __repr__(self):
        """
        for representaions of queue elemetns
        """
        return self.display()

    def __len__(self):
        """
        for length of queue object
        """    
        return self.size()         

    def __iter__(self):   
        """
        queue elements iterations from front to rear
        """
        if self.is_empty():
            raise IndexError("Queue object is not iterable Because Queue is empty")        
        i = 0
        while True:
            if i >= len(self.items):
                raise StopIteration
            yield self.items[i]
            i += 1   


    def size(self):
        """ 
        return the size of queue 
        Syntax: size()  
        Time Complexity: O(1)  
        """   
        return len(self.items) 

    def peek(self):
        """
        function to return the front element value
        Syntax: peek()  
        Time Complexity: O(1)  
        """
        if self.is_empty():
            raise IndexError("Front element doesnot exixts Because Queue is empty")
        return self.items[0]

    def is_empty(self):
        """ 
        return the true if queue is empty
        Syntax: is_empty()  
        Time Complexity: O(1)   
        """   
        return self.items == []
   
    def display(self):
        """ 
        function to display the queue elements
        Syntax: display()  
        Time Complexity: O(1)  
        """ 
        #if queue is empty
        if(len(self.items)<=0):
            print("Queue is Empty ",end='')
            return str() #for representaion purpose
        # otherwise
        else:
            print('-'*11,'Queue','-'*11)
            print('Front : '+str(self.items[0]))
            print('Rear : '+str(self.items[-1]))
            print('Elements : '+str(self.items))
            print('Size : '+str(len(self.items)))
            print('-'*30)
        return str() #for representaion purpose

    def enqueue(self,item):
        """ 
        function to insert a given element on rear end of queue
        Syntax: enqueue(item)  
        Time Complexity: O(1)  
        """
        #adding element at rear end
        self.items.append(item)


    def dequeue(self):
        """ 
        function to delete element from front end of queue
        Syntax: dequeue(item)  
        Time Complexity: O(1)          
        """        
        #if queue is empty
        if self.is_empty():
            raise IndexError("Deletion is not Possible Because Queue is Empty")
        else:
            item = self.items[0]
            del self.items[0] # deleting front element
            return item   








if __name__ == '__main__':
    obj=Stack()
    while(1):
        print("\n------------")
        print("Stack Menu")
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Exit")
        print("------------")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            item=input("\nEnter the element you want to insert in stack : ")
            obj.push(item)
        elif(choice==2):
            item=obj.pop()
            print("\nThe Poped element is : ",item)
        elif(choice==3):
            item=obj.peek()
            print("\nThe Top element is : ",item)   
        elif(choice==4):
            print("Exiting ....")
            break
        else:
            continue
        

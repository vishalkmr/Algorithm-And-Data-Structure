'''
 Implementation of Queue Data Structure using basic list operations
'''

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
    obj=Queue()
    while(1):
        print("\n------------")
        print("Queue Menu")
        print("1.Enqueue")
        print("2.Dequeue")
        print("3.Peek")
        print("4.Display")
        print("5.Exit")
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
            obj.display()  
        elif(choice==5):
            print("\nExiting ......")
            break
        else:
            continue
 
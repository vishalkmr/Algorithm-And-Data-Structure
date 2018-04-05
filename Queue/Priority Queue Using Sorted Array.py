'''
 Implementation of Priority Queue Data Structure using Sorted Array
 Priority Queue returns the Highest Priority element on Dequeue Operation
 Assume higher value of queue element have higher priority represent '
 
 Example 
 If Queue contains 2,3,1,45,6,23,33
 then dequeue operation return 45
'''

class Priority_Queue:
    """Class to implement Priority Queue Data Structure using Sorted Array"""
    def __init__(self):
        """
        constructing a queue 
        """
        self.items=[]
    
    def __str__(self):
        """
        for printing the Priority Queue elemetns
        """
        return self.display()

    def __repr__(self):
        """
        for representaions of Priority Queue elemetns
        """
        return self.display()

    def __len__(self):
        """
        for length of Priority Queue object
        """    
        return self.size()         

    def __iter__(self):   
        """
        queue elements Priority Queue from front to rear
        """
        if self.is_empty():
            raise IndexError("Priority Queue object is not iterable Because Queue is empty")        
        i = 0
        while True:
            if i >= len(self.items):
                raise StopIteration
            yield self.items[i]
            i += 1   


    def size(self):
        """ 
        return the size of Priority Queue 
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
            raise IndexError("Front element doesnot exixts Because Priority Queue is empty")
        return self.items[0]

    def is_empty(self):
        """ 
        return the true if Priority Queue is empty
        Syntax: is_empty()  
        Time Complexity: O(1)   
        """   
        return self.items == []
   
    def display(self):
        """ 
        function to display the Priority Queue elements
        Syntax: display()  
        Time Complexity: O(1)  
        """ 
        #if Priority Queue is empty
        if(len(self.items)<=0):
            print("Priority Queue is Empty ",end='')
            return str() #for representaion purpose
        # otherwise
        else:
            print('-'*11,'Priority Queue','-'*11)
            print('Front : '+str(self.items[0]))
            print('Rear : '+str(self.items[-1]))
            print('Elements : '+str(self.items))
            print('Size : '+str(len(self.items)))
            print('-'*30)
        return str() #for representaion purpose

    def enqueue(self,item):
        """ 
        function to insert a given element in Priority Queue
        Syntax: enqueue(item)  
        Time Complexity: O(n)  
        """
        #since we are using sorted array so we have ensure that the Priority Queue items are remains in sorted manner even after adding new item
        
        self.items.append(item) #1st adding the new item at the end of the Priority Queue
        i=len(self.items)-1

        #then perform pairwise swap until the new item it adjusted to its appropriate postion in sorted items
        while i>0:
        	if self.items[i]>self.items[i-1]:
        		self.items[i],self.items[i-1]=self.items[i-1],self.items[i]
        	i-=1
        


    def dequeue(self):
        """ 
        function to delete highest priority element from Priority Queue
        Syntax: dequeue(item)  
        Time Complexity: O(1)          
        """        
        #if Priority Queue is empty
        if self.is_empty():
            raise IndexError("Deletion is not Possible Because Priority Queue is Empty")
        else:
        	#since we are using sorted array so the first element have highest priority element
            highest=self.items[0]
            del self.items[0] # deleting highest priority element
            return highest   




if __name__ == '__main__':
    obj=Priority_Queue()
    while(1):
        print("\n------------")
        print("Priority Queue Menu")
        print("1.Enqueue")
        print("2.Dequeue")
        print("3.Peek")
        print("4.Display")
        print("5.Exit")
        print("------------")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            item=int(input("\nEnter the element you want to insert in Priority Queue : "))
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
 
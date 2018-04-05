'''
 Implementation of Deque Data Structure using basic list operations
'''

class Deque:
    """Class to implement Deque Data Structure using basic list operations"""
    def __init__(self):
        """
        constructing a Deque 
        """
        self.items=[]
    
    def __str__(self):
        """
        for printing the Deque elemetns
        """
        return self.display()

    def __repr__(self):
        """
        for representaions of Deque elemetns
        """
        return self.display()

    def __len__(self):
        """
        for length of deque object
        """    
        return self.size()         

    def __iter__(self):   
        """
        deque elements iterations from front to rear
        """
        if self.is_empty():
            raise IndexError("Deque object is not iterable Because deque is empty")        
        i = 0
        while True:
            if i >= len(self.items):
                raise StopIteration
            yield self.items[i]
            i += 1   


    def size(self):
        """ 
        return the size of deque 
        Syntax: size()  
        Time Complexity: O(1)  
        """   
        return len(self.items) 


    def front(self):
        """
        function to return the front element value
        Syntax: front()  
        Time Complexity: O(1)  
        """
        if self.is_empty():
            raise IndexError("Front element doesnot exixts Because Deque is empty")
        return self.items[0]


    def rear(self):
        """
        function to return the rear element value
        Syntax: rear()  
        Time Complexity: O(1)  
        """
        if self.is_empty():
            raise IndexError("Rear element doesnot exixts Because Deque is empty")
        return self.items[-1]


    def is_empty(self):
        """ 
        return the true if deque is empty
        Syntax: is_empty()  
        Time Complexity: O(1)   
        """   
        return self.items == []
   
    def display(self):
        """ 
        function to display the deque elements
        Syntax: display()  
        Time Complexity: O(1)  
        """ 
        #if deque is empty
        if(len(self.items)<=0):
            print("Deque is Empty ",end='')
            return str() #for representaion purpose
        # otherwise
        else:
            print('-'*11,'Deque','-'*11)
            print('Front : '+str(self.items[0]))
            print('Rear : '+str(self.items[-1]))
            print('Elements : '+str(self.items))
            print('Size : '+str(len(self.items)))
            print('-'*30)
        return str() #for representaion purpose

    def add_front(self,item):
        """ 
        function to insert a given element on front end of deque
        Syntax: add_front(item)  
        Time Complexity: O(1)  
        """
        #adding element at front end
        self.items.insert(0,item)

    def add_rear(self,item):
        """ 
        function to insert a given element on rear end of deque
        Syntax: add_rear(item)  
        Time Complexity: O(1)  
        """
        #adding element at rear end
        self.items.append(item)

    def delete_front(self):
        """ 
        function to delete element from front end of deque
        Syntax: delete_front(item)  
        Time Complexity: O(1)          
        """        
        #if deque is empty
        if self.is_empty():
            raise IndexError("Deletion is not Possible Because deque is Empty")
        else:
            item = self.items[0]
            del self.items[0] # deleting front element
            return item   


    def delete_rear(self):
        """ 
        function to delete element from rear end of deque
        Syntax: delete_rear(item)  
        Time Complexity: O(1)          
        """        
        #if deque is empty
        if self.is_empty():
            raise IndexError("Deletion is not Possible Because deque is Empty")
        else:
            item = self.items[-1]
            del self.items[-1] # deleting rear element
            return item   


if __name__ == '__main__':
    obj=Deque()
    while(1):
        print("\n------------")
        print("Deque Menu")
        print("1.Add Front")
        print("2.Add Rear")
        print("3.Delete Front")
        print("4.Delete Rear")
        print("5.Display")
        print("6.Exit")
        print("------------")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            item=input("\nEnter the element you want to insert in deque : ")
            obj.add_front(item)
        if(choice==2):
            item=input("\nEnter the element you want to insert in deque : ")
            obj.add_rear(item)
        elif(choice==3):
            item=obj.delete_front()
            print("\nThe deleted element is : ",item)
        elif(choice==4):
            item=obj.delete_rear()
            print("\nThe deleted element is : ",item)
        elif(choice==5):
            obj.display()  
        elif(choice==6):
            print("\nExiting ......")
            break
        else:
            continue
 
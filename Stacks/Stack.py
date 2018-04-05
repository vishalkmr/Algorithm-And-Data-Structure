'''
 Implementation of Stack Data Structure using basic list operations
'''

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
    obj=Stack()
    while(1):
        print("\n------------")
        print("Stack Menu")
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Display")
        print("5.Exit")
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
            obj.display()  
        elif(choice==5):
            print("Exiting ....")
            break
        else:
            continue
        

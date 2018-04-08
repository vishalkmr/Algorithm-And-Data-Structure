
class Node:
    """Class to implement Self Refrential Class Node"""
    def __init__(self, data=None, next=None):
        """
        constructing a Node 
        """
        self.data = data
        self.next  = next

    def __str__(self):
        """
        for printing Node data
        """       
        return str(self.data)

    def __repr__(self):
        """
        for representaions of Node data
        """       
        return str(self.data)

class LinkedList:
    """Class to implement Singly-Linked-List"""
    def __init__(self):
        """
        constructing a Linked-List and 
        initializing size=0 
        """
        self.head = None
        self.tail=None
        self.size = 0
     
    def __str__(self):
        """
        for printing Linked-List elements
        """
        return self.traversal()

    def __repr__(self):
        """
        for representaions of Linked-List elements
        """
        return self.traversal()   

    def __len__(self):
        """
        for length of Linked-List 
        """    
        return self.size         

    def __iter__(self):   
        """
        Linked-List elements iterations from beginning to end
        """
        if self.size==0:
            raise IndexError("Linked-List object is not iterable Because Linked-List is empty")        
        ptr = self.head
        while True:
            if not ptr:
                raise StopIteration
            yield ptr.data
            ptr=ptr.next   

       
    def traversal(self):
        """
        Function to traverse the elements of linked-list
        Syntax: traversal() 
        Time Complexity: O(n)         
        """
       # if linked-list is empty
        if self.size==0:
            print('Linked-List is Empty ',end='')
            return str() #for representaion purpose 

        ptr = self.head
        print('-'*17,'Linked-List','-'*17)
        print(' Head : '+str(self.head.data))
        print(' Tail : '+str(self.tail.data))
        while ptr is not None:
            print(' '+str(ptr.data),end=' ==>')
            ptr = ptr.next
        print('NULL')
        print(' Size : '+str(self.size))
        print('-'*47)
        return str() #for representaion purpose 

    
    def insert_beginning(self, data):    
        """
        Function to insert new node at the beginning of linked-list
        Syntax: insert_beginning(data) 
        Time Complexity: O(1)   
        """
        self.size = self.size + 1
        new_node = Node(data) #creating new node
        
        # if linked-list is empty
        if not self.head:
            self.head = new_node
            self.tail=new_node
        
        #if some element exists in linked-list
        else:
            new_node.next = self.head
            self.head = new_node
  

    def insert_end(self, data):
        """
        Function to insert new node at the end of linked-list
        Syntax: insert_end(data) 
        Time Complexity: O(1)           
        """    
        self.size = self.size + 1
        new_node = Node(data) #creating new node
        
        # if linked-list is empty
        if not self.head:
            self.head = new_node
            self.tail=new_node

        #if some element exists in linked-list
        else:
            self.tail.next=new_node #appending the newnode at the end
            self.tail=new_node #updating the tail


    def insert(self, data,index):
        """
        Function to insert new node at the given postion in linked-list
        Syntax: insert(data,index) 
        Index :simmilar to array indexing
        Time Complexity: O(n)           
        """    
        if(index==self.size+1):
            raise IndexError("Insertion is not Possible Because given index doesnot exists") 

        elif(index==0):
            self.insert_beginning(data)
        
        elif(index==self.size):
            self.insert_end(data)
        
        else:                
            new_node = Node(data) #creating new node
            counter=0
            previous=None
            current=self.head

            #iterating until we reach at desired index
            while current is not None and counter!=index:
                previous=current
                current=current.next 
                counter+=1

            #if that index is reached then simply insert the node between current node and prevoius node
            if counter==index :
                self.size = self.size + 1
                previous.next=new_node
                new_node.next=current  
                    
        
    def delete_beginning(self):    
        """
        Function to delete items from the beginning of linked-list
        Returns the deleted element
        Syntax: delete_beginning() 
        Time Complexity: O(1)           
        """
        # if linked-list is empty
        if self.size==0:
            raise IndexError("Deletion is not Possible Because Linked-List is Empty")       

        self.size = self.size - 1
        data=self.head.data
        ptr=self.head
        self.head=self.head.next #updating the head of linked-list to points to next node
        del ptr #deallocating the memory
        return data

    def delete_end(self):    
        """
        Function to delete items from the end of linked-list
        Returns the deleted element
        Syntax: delete_end() 
        Time Complexity: O(n)          
        """
        # if linked-list is empty
        if self.size==0:
            raise IndexError("Deletion is not Possible Because Linked-List is Empty")

        #if only one node is present    
        elif self.size==1:
            data=self.head.data
            self.head=None
            self.tail=None
            self.size=0
            return data        


        self.size = self.size - 1
        previous=None
        current=self.head

        #iterating until current points to last element of linked-list
        while current.next is not None:
            previous=current
            current=current.next 

        data=current.data
        previous.next=None   
        self.tail=previous     #updating tail
        del current #deallocating the memory
        return data


    def delete(self, data):
        """
        Function to delete given items from the linked-list
        Returns the true if element is deleted
        Syntax: remove(data) 
        Time Complexity: O(n)           
        """
        # if linked-list is empty
        if self.size==0:
            raise IndexError("Deletion is not Possible Because Linked-List is Empty")

                 
        current = self.head
        previous = None
        
        while current and current.data != data :
            previous = current
            current = current.next
        try:
                
            # if node to be deleted is head node    
            if previous is None:
                ptr=self.head
                self.head = current.next
                del ptr
            else:
                #if node is last node the update the tail
                if current.data == self.tail.data:
                    self.tail=previous
                ptr=current
                previous.next = current.next     
                del ptr
            self.size = self.size - 1 
            return True   
            
        except:
            return False        
        



if __name__ == '__main__':
    obj=LinkedList()
    while(1):
        print("\n--------------------------------------------------------------")
        print("Queue Menu")
        print("1.Insert at Beginning")
        print("2.Insert at End")
        print("3.Insert at Given Postion")
        print("4.Delete from Beginning")
        print("5.Delete from End")
        print("6.Remove Given Node")
        print("7.Traversal")
        print("8.Exit")
        print("--------------------------------------------------------------")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            data=input("\nEnter the element you want to insert in Linked-List : ")
            obj.insert_beginning(data)
        elif(choice==2):
            data=input("\nEnter the element you want to insert in Linked-List : ")
            obj.insert_end(data)
        elif(choice==3):
            data=input("\nEnter the element you want to insert in Linked-List : ")
            index=int(input('\nEnter the Postion where you want to insert the element : '))
            obj.insert(data,index)
        elif(choice==4):
            data=obj.delete_beginning()  
            print('\nDeleted element is : ',data)
        elif(choice==5):
            data=obj.delete_end()  
            print('\nDeleted element is : ',data)
        elif(choice==6):
            data=input("\nEnter the data of node you want to delete from Linked-List : ")
            if obj.delete(data):
                print('\nDeletion Successful')
            else:
                print('\nDeletion Failed ')
        elif(choice==7):
            obj.traversal()           
        elif(choice==8):
            print('\nExiting.......')
            break
        else:
            continue

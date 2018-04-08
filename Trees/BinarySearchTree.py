
class Node:
    """Class to implement TreeNode"""
    def __init__(self, data=None, right=None,left=None):
        """
        constructing a TreeNode 
        """
        self.data = data
        self.right  = right
        self.left = left

    def __str__(self):
        """
        for printing TreeNode data
        """       
        return str(self.data)

    def __repr__(self):
        """
        for representaions of TreeNode data
        """
        return str(self.data)

class BinarySearchTree:
    """Class to implement Binary Search Tree"""
    def __init__(self):
        """
        constructing a BinarySearchTree 
        """
        self.root = None
        self.nodes  =0


    def insert(self,root,data):
        #if no nodes present in the BST
        if self.nodes==0:           
            self.root=Node(data)
            self.nodes+=1
        
        #otherwise find the appropriate postion for the new node in BST
        else:
            if root.left==None and data < root.data:
                self.nodes+=1
                root.left=Node(data)
            
            elif root.right==None and data >= root.data:    
                self.nodes+=1
                root.right=Node(data)
            
            elif data < root.data:
                self.insert(root.left,data)
            
            else:
                self.insert(root.right,data)
        
    def search(self,root,data):
        if root==None:
            return None
        if root.data==int(data):
            return root
        elif root.data < int(data):
            return self.search(root.right,data)
        else:
            return self.search(root.left,data)            
            
    def delete(self,data):
         target=self.search(self.root,data)
         
         parent=self.parent(self.root,target)

         print(target)
         # print(predessor)
         print(parent)

         #0 childs
         if target.left==None and target.right==None:
            print('0')
            if parent.left==target:
                parent.left==None
            else:
                parent.right=None
         
         #1 left childs
         elif target.left!=None and target.right==None:
            print('1 left')
            if parent.left==target:
                parent.left==target.left
            else:
                parent.right=target.left                
         
         #1 right childs       
         elif target.left==None and target.right!=None:
            print('1 right')
            if parent.left==target:
                parent.left==target.right
            else:
                parent.right=target.right
         
         else:
            print('2')
            successor=self.successor(target)
            target.data=successor.data
            self.delete(self.root,successor)




    def parent(self,root,node):
        if root==None:
            return None   
        if root.left==node or root.right==node:
            return root
        elif root.data<=node.data:
            return self.parent(root.right,node)
        else:
            return self.parent(root.left,node) 

    def successor(self,node):
        node=node.right
        while node.left!=None:
            node=node.left
        return node 
           
    def predessor(self,node):
        node=node.left
        while node.right!=None:
            node=node.right
        return node

    def display(self):
        if self.nodes==0:
            print('Binary Search Tree is Empty')
            return

        print('-'*10+'Binary Search Tree'+'-'*10)
        print('Nodes  : '+str(self.nodes))
        print('Inorder Traversal :',end='')
        self.inorder(self.root)
        print()
        print('Preorder Traversal :',end='')
        self.preorder(self.root)
        print()
        print('Postorder Traversal :',end='')
        self.postorder(self.root)
        print()
        print('-'*30)


    def inorder(self,root):
        """
        Function to find Inorder traversal of the Binary Search Tree
        Syntax: inorder() 
        Time Complexity: O(n) 
        Recurrence Relation :
            Best Case : T(n)=2T(n/2)+C (C represents constant)    
            Worst Case : T(n)=T(n-1)+C  (C represents constant)         
        """
        # if Tree is empty
        if not root:
            return 

        self.inorder(root.left) #left
        print(root.data,end=' ')    #root
        self.inorder(root.right) #right


    def preorder(self,root):
        """
        Function to find Preorder traversal of the given Tree
        Syntax: inorder(root) 
        Time Complexity: O(n)
        Recurrence Relation :
            Best Case : T(n)=2T(n/2)+C (C represents constant)    
            Worst Case : T(n)=T(n-1)+C  (C represents constant)       
        """
       # if Tree is empty
        if not root:
            return 

        print(root.data,end=' ')    #root    
        self.preorder(root.left) #left
        self.preorder(root.right) #right
    
    def postorder(self,root):
        """
        Function to find Postorder traversal of the given Tree
        Syntax: inorder(root) 
        Time Complexity: O(n)      
        Recurrence Relation :
            Best Case : T(n)=2T(n/2)+C (C represents constant)    
            Worst Case : T(n)=T(n-1)+C  (C represents constant) 
        """
       # if Tree is empty
        if not root:
            return 

        self.postorder(root.left) #left
        self.postorder(root.right) #right
        print(root.data,end=' ')    #root


if __name__ == '__main__':
    bst=BinarySearchTree()
    while(1):
        print("\n--------------------------------------------------------------")
        print("Binary Search Tree Menu")
        print("1.Insertion")
        print("2.Deletetion")
        print("3.Search")        
        print("4.Traversal")
        print("5.Exit")
        print("--------------------------------------------------------------")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            data=int(input("\nEnter the element you want to insert in Binary Search Tree : "))
            bst.insert(bst.root,data)
        elif(choice==2):
            data=input("\nEnter the data of node you want to delete from Binary Search Tree : ")
            if bst.delete(data):
                print('\nDeletion Successful')
            else:
                print('\nDeletion Failed ')
        elif(choice==3):
            data=int(input("\nEnter the element you want to Search in Binary Search Tree : "))
            if bst.search(bst.root,data):
                print('Search Successful')
            else:
                print('Search UnSuccessful')
        elif(choice==4):
            bst.display()           
        elif(choice==5):
            print('\nExiting.......')
            break
        else:
            continue
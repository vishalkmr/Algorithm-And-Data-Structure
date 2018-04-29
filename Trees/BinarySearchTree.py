
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
        
        #otherwise recursively find out the appropriate postion for the new node in BST
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
         
         if not target:
            return False
         # if target is self.root:
         #    print('root')
         #    predessor=self.predessor(target)
            
         #    # if predessor:
            #     target.data=predessor.data
            #     self.delete(predessor)
            # else:
            #     successor=self.successor(target)
            #     target.data=successor.data
            #     self.delete(successor)
                    

         parent=self.parent(self.root,target)

         print(target)
         # print(predessor)
         print(parent)

         #Deletion of leaf node 
         if target.left==None and target.right==None:
            if parent.left is target:
                print('0 left')
                parent.left==None
            
            else:
                print('0 right')
                parent.right=None

            del target
            self.nodes-=1
            return True
         
         #When node have only left child
         elif target.left!=None and target.right==None:
            if parent.left is target:
                print('1 left left')
                parent.left==target.left
                
            else:
                print('1 left right')
                parent.right=target.left             
            
            del target
            self.nodes-=1
            return True

         #When node have only right child
         elif target.left==None and target.right!=None:
            if parent.left is target:
                print('1 right left')
                parent.left==target.right

            else:
                print('1 right right')
                parent.right=target.right

            del target
            self.nodes-=1
            return True

         #Deletion of intermediate node
         elif target.left!=None and target.right!=None:
            print('2')
            predessor=self.predessor(target)
            temp=predessor.data
            self.delete(predessor)
            target.data=predessor.data




    def parent(self,root,node):
        if root==None:
            return None   
        if root.left is node or root.right is node:
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
            data=int(input("\nEnter the data of node you want to delete from Binary Search Tree : "))
            if bst.delete(data):
                print('\nDeletion Successful')
            else:
                print('\nDeletion Failed ')
        elif(choice==3):
            data=int(input("\nEnter the element you want to Search in Binary Search Tree : "))
            result=bst.search(bst.root,data)
            if result!=False:
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
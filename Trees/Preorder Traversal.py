'''
 Display PreOrder Traversal of a given Binary tree
 Exapmle :
                 1
                /  \
              2      3
             / \    / \
            4   5  6   7

Preorder Traversal : 1,2,4,5,3,6,7
'''


from TreeNode import Node

#using Recursion
def preorder(root):
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

    print(root.data)    #root    
    preorder(root.left) #left
    preorder(root.right) #right

#using Stack
def preorder(root):
    """
    Function to find preorder traversal of the given Tree
    Syntax: preorder(root) 
    Time Complexity: O(n) 
    """
    current=root
    stack=[]
    
    #move to the left most leaf node
    while current != None:
        print(current.data) #while moving print the nodes data        
        
        #if node have right children 
        if current.right!=None:                
          stack.append(current.right) 
        
        current=current.left
    
    #now perform the backtracking and print the remaning nodes
    while len(stack)!=0:
        item=stack.pop()
        current=item
        #again move to the left most leaf node
        while current != None:
            print(current.data) #while moving print the nodes data        
            #if node have right children 
            if current.right!=None:                
              stack.append(current.right) 
            current=current.left


 


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g

preorder(a)

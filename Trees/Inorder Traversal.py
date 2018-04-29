'''
 Display Inorder Traversal of a given Binary tree
 Exapmle :
                 1
                /  \
              2      3
             / \    / \
            4   5  6   7

Inorder Traversal : 4,2,5,1,6,3,7
'''


from TreeNode import Node

#using Recursion
def inorder(root):
    """
    Function to find Inorder traversal of the given Tree
    Syntax: inorder(root) 
    Time Complexity: O(n) 
    Recurrence Relation :
        Best Case : T(n)=2T(n/2)+C (C represents constant)    
        Worst Case : T(n)=T(n-1)+C  (C represents constant)         
    """
   # if Tree is empty
    if not root:
        return 

    inorder(root.left) #left
    print(root.data)    #root
    inorder(root.right) #right
    
#using Stack
def inorder(root):
    """
    Function to find Inorder traversal of the given Tree
    Syntax: inorder(root) 
    Time Complexity: O(n) 
	"""
    current=root
    stack=[]
    
    #move to the left most leaf node
    while current != None:
        stack.append(current) #while moving push node onto stack
        current=current.left
    
    #now perform the backtracking and print the nodes data
    while len(stack)!=0:
        item=stack.pop()
        print(item.data)

        #if node have right children then again move to the left most leaf node
        if item.right!=None:
            current=item.right
            while current != None:
                stack.append(current) #while moving push node onto stack
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
inorder(a)

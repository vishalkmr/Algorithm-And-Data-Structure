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
    

a=Node('1')
b=Node('2')
c=Node('3')
d=Node('4')
e=Node('5')
f=Node('6')
g=Node('7')
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
inorder(a)

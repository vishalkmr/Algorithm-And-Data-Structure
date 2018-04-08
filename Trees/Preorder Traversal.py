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
preorder(a)

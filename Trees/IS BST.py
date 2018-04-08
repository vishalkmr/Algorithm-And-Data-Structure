'''
 Find the given Binary tree is Binary Search Tree(BST) or not.
 For BST Leftsubtree nodes data < Root node data < Rightsubtree nodes data

 Exapmle :
                  4
                /  \
              2      6
             / \    / \
            1   3  5   7

 Returns : True
'''
from TreeNode import Node


def is_bst(root):
    """
    Function returns True if the given Binary tree is Binary Search Tree  
    Syntax: is_bst(root) 
    Time Complexity: O(n)              
    """
   # if Tree is empty
    if not root:
        return True 

    #if leaf node 
    elif root.left==None and root.right==None:
      return True
    
    #intermidiate node with two children
    elif root.left!=None and root.right!=None:  
        if root.left.data <=root.data and root.data <= root.right.data :
            return is_bst(root.left) and is_bst(root.right)
        else:
            return False
    
    #intermidiate node with left children only
    elif root.left!=None:
        if root.left.data <=root.data :
            return is_bst(root.left)
        else:
            return False

    #intermidiate node with right children only
    elif root.right!=None :   
        if  root.data <= root.right.data :
           return is_bst(root.right)
        else:
            return False
  
    # return False




n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)

n4.left=n2
n4.right=n6
n2.left=n1
n2.right=n3
n6.left=n5
n6.right=n7


result=is_bst(n4)
print(result)
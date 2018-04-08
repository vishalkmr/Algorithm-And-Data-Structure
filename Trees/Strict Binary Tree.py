'''
 Find the given Binary tree is Strict Binary Tree(Balanced Binary) or not.
 Strict binary tree have either 0 childs or 2 childs

 Exapmle :
                  1
                /  \
              2      3
             / \    / \
            4   5  6   7

 Returns : True
'''


from TreeNode import Node


def strict_binary_tree(root):
    """
    Function returns True if the given Binary tree is Strict Binary Tree  
    Syntax: strict_binary_tree(root) 
    Time Complexity: O(n)
    Recurrence Relation :
        Best Case : T(n)=C (C represents constant)    
        Worst Case : T(n)=2T(n/2)+C  (C represents constant)              
    """
   # if Tree is empty
    if not root:
        return True 

    #if leaf node 
    if root.left==None and root.right==None:
      return True

    if root.left!=None and root.right!=None:
    	return strict_binary_tree(root.left) and strict_binary_tree(root.right) 
    else:
    	return False

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


result=strict_binary_tree(a)
print(result)
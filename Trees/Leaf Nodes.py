'''
 Find the number leaf Nodes in a given Binary tree
 Exapmle :
                 1
                /  \
              2      3
             / \    / \
            4   5  6   7

 Leaf Nodes : 4 (i.e. 4,5,6,7)
'''


from TreeNode import Node


def leaf(root):
    """
    Function to Find the number leaf Nodes in a given Binary tree
    Syntax: leaf(root) 
    Time Complexity: O(n)  
    Recurrence Relation :
        Best Case : T(n)=2T(n/2)+C (C represents constant)    
        Worst Case : T(n)=T(n-1)+C  (C represents constant)          
    """
   # if Tree is empty
    if not root:
        return 0 

    #if leaf node return leaf count as 1
    if root.left==None and root.right==None:
      return 1

    #recursively compute leaf nodes in left and right subtree 
    left_subtree_leaf=leaf(root.left)
    right_subtree_leaf=leaf(root.right)

    #add them to get total leaf in whole tree
    total_leaf =left_subtree_leaf+right_subtree_leaf

    return total_leaf
    
    

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

result=leaf(a)
print(result)
'''
 Find the number intermedaite(non-leaf) Nodes in a given Binary tree
 Exapmle :
                 1
                /  \
              2      3
             / \    / \
            4   5  6   7

 intermedaite(Non-Leaf) Nodes : 3 (i.e. 1,2,3)
'''


from TreeNode import Node


def non_leaf(root):
    """
    Function to Find the number intermedaite Nodes(Non-Leaf) in a given Binary tree
    Syntax: non_leaf(root) 
    Time Complexity: O(n) 
    Recurrence Relation :
        Best Case : T(n)=2T(n/2)+C (C represents constant)    
        Worst Case : T(n)=T(n-1)+C  (C represents constant)         
    """
   # if Tree is empty
    if not root:
        return 0 

    #if leaf node 
    if root.left==None and root.right==None:
      return 0

    #recursively compute intermediate nodes in left and right subtree 
    left_subtree_non_leaf=non_leaf(root.left)
    right_subtree_non_leaf=non_leaf(root.right)

    #compute the total intermediates node by considering current intermediate node , left_subtree_non_leaf node and right_subtree_non_leaf node
    total_non_leaf=left_subtree_non_leaf+right_subtree_non_leaf+1
    
    return total_non_leaf
 
    
    

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

result=non_leaf(a)
print(result)
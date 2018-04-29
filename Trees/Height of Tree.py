'''
 Find the Height of a given Binary tree.
 Height is the length of longest path from root node to leaf node.

 Exapmle :
                 1            height-4      level-5
                /  \
              2      3        height-3      level-4    
             / \    / 
            4   5  6          height-2      level-3
           /    
          7                   height-1      level-2
         / 
        8                     height-0      level-1

 Height : 4
'''


from TreeNode import Node


def height(root):
    """
    Function to Find the height of the given Binary tree
    Syntax: height(root) 
    Time Complexity: O(n)   
    Recurrence Relation :
        Best Case : T(n)=2T(n/2)+C (C represents constant)    
        Worst Case : T(n)=T(n-1)+C  (C represents constant)       
    """
   # if Tree is empty
    if not root:
        return 0 

    #if leaf node return 0 (Bcz. leaf node is present at height 0)
    if root.left==None and root.right==None:
      return 0

    #recursively compute the height of left and right subtree 
    left_subtree_height=height(root.left)
    right_subtree_height=height(root.right)

    #compute the overall height of tree
    total_height =max(left_subtree_height,right_subtree_height)+1

    return total_height
    
    

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
h=Node(8)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
d.left=g
g.left=h

result=height(a)
print(result)
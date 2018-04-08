'''
 Find the Number of Levels of in a given Binary tree.
 Levels = Height+1

 Exapmle :
                 1
                /  \
              2      3
             / \    / 
            4   5  6   
           /    
          7
         / 
        8 
			
 Levels : 5
'''


from TreeNode import Node


def levels(root):
    """
    Function to Find the number of levels of in the given Binary tree
    Syntax: levels(root) 
    Time Complexity: O(n)
    Recurrence Relation :
        Best Case : T(n)=2T(n/2)+C (C represents constant)    
        Worst Case : T(n)=T(n-1)+C  (C represents constant)          
    """
   # if Tree is empty
    if not root:
        return 0 

    #if leaf node return 1 (Bcz. leaf node is present at 0th level)
    if root.left==None and root.right==None:
      return 1

    #recursively compute the levels of left and right subtree 
    left_subtree_levels=levels(root.left)
    right_subtree_levels=levels(root.right)

    #compute the overall levels of tree
    total_levels =max(left_subtree_levels,right_subtree_levels)+1

    return total_levels
    
    

a=Node('1')
b=Node('2')
c=Node('3')
d=Node('4')
e=Node('5')
f=Node('6')
g=Node('7')
h=Node('8')
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
d.left=g
g.left=h

result=levels(a)
print(result)
'''
 Check the given two Binary tree are equal or not
  Exapmle :   Tree 1                Tree 2
                  1                   1
                /  \                 / \
              2      3             2     3
             / \    / \           / \   / \
            4   5  6   7         4  5  6   7
				
 Returns : True
'''


from TreeNode import Node


def equal(root1,root2):
    """
    Return True if both of the tree are equal
    Syntax: mirror_image(root1,root2) 
    Time Complexity: O(n)
    """
   #For Empty Tree
    if root1==None and root2==None:
        return True

    #For leaf node
    if root1.left==None and root1.right==None and root2.left==None and root2.right==None and root1.data==root2.data:
        return True

    #if root data is mathched then recursilvely match there left and right subtrees    
    if root1.data==root2.data:
        return equal(root1.left,root2.left) and equal(root1.right,root2.right)  

    else:
        return False





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


a1=Node(1)
b1=Node(2)
c1=Node(3)
d1=Node(4)
e1=Node(5)
f1=Node(6)
g1=Node(7)
a1.left=b1
a1.right=c1
b1.left=d1
b1.right=e1
c1.left=f1
c1.right=g1



result=equal(a,a1)
print(result)
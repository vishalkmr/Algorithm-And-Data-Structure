
class Node:
    """Class to implement TreeNode"""
    def __init__(self, data=None, right=None,left=None):
        """
        constructing a TreeNode 
        """
        self.data = data
        self.right  = right
        self.left = left

    def __str__(self):
        """
        for printing TreeNode data
        """       
        return str(self.data)

    def __repr__(self):
        """
        for representaions of TreeNode data
        """
        return str(self.data)




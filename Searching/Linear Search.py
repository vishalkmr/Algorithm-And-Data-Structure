'''
    Linear Search best suited for Unsorted lists
'''


def linear_search(list,item):
    """
    funtion for linear search of element in list
    syntax: linear_search(list,item)
    return index value where the item is found
    Time Complexity: O(n) 
    """
    length=len(list)
    i=0
    while(i<length):
        if(list[i]==item):
            return i
        i=i+1


list=[0,1,2,3,4,5,6,7]
item=3
result=linear_search(list,item)

if result!=None:
    print(result)
else:
    print('Not Found !')
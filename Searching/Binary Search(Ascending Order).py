'''
 Binary Search on Ascending order Lists
 Assume that list is in Ascending order
 Binary search is aplicable only when list is Sorted
'''

def binary_search(list,item):
    ''' 
    funtion for binary search of element in list
    synatx: binary_search( list,item)
    retrun index of element where the item is found
    return -1 when item is not found in list
    Time Complexity: O(logn)
    '''
    beg=0
    length=len(list)
    end=length-1
    mid=(beg+end)//2 #finding middle element index

    while(beg<=end):            
        #if item is mathched with middle element
        if(list[mid]==item):
            return mid
        
        #if item is less than the middle element than consider only left portion of list
        elif(list[mid]>item):
            end=mid-1
        
        #if item is greater than the middle element than consider only right portion of list
        elif(list[mid]<item):
            beg=mid+1
        
        mid=(beg+end)//2 #finding middle element index
    
    if(beg>end ):
        return -1



list=[0,1,2,3,4,5,6,7]
item=6
result=binary_search(list,item)

if result== -1:
    print("Not Found !")
else:
    print(result)
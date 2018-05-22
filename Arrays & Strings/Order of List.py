'''
 Check weather list is in Ascending order/ Descending order / Not in Order

 Example
 check_order([1,2,3,4,5,6,7])
 Returns: 1
'''


def check_order(list):
    '''
    function to check weather list is in ascending order ,descending order or none        
    synatx: check_order( list,item)
    return 1 when list is in ascending order
    return -1 when list is in descending order
    return 0  when list is niether in ascending order or descending order
    Time Complexity: O(n)
	'''
    length=len(list)

    # to check the list is in ascending order
    for i in range(length-1):
        if(list[i]>list[i+1]):
                break
        if i==length-2:
            return 1                     

    # to check the list is in descending order
    for i in range(length-1):
        if(list[i]<list[i+1]):
            break
        if i==length-2:
            return -1 
    
    # otherwise list is not sorted
    return 0
		

list=[7, 6, 5, 4, 3, 2, 1]
result=check_order(list)

if result==1:
	print('Ascending')
elif result==-1:
	print('Descending')
else:
	print('Not Sorted')
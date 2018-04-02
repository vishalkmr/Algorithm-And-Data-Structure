'''
 Binary Search using Recursion
 Assume that list is already in Ascending order.

 Space Complexity of Binary Search using Recursion is more than simple Binary Search 
 Becuase it make use of Recursion Stack for each function call
'''



def binary_search(list,lower,upper,item):
	''' 
	    funtion for binary search of element in list 
	    synatx: binary_search( list,lower,upper,item)
	    return index of element where the item is found
	    Time Complexity: O(logn) 
	    Space Complexity: O(logn) 
	'''
	if lower<=upper:
		middle=(lower+upper)//2 #finding middle element index

		#if item is mathched with middle element
		if list[middle]==item:
			return middle

		#if item is greater than the middle element than apply Binary Search on right portion of list
		elif list[middle]<item:
			return  binary_search(list,middle+1,upper,item)

		#if item is greater than the middle element than apply Binary Search on left portion of list
		else:
			return binary_search(list,lower,middle-1,item)	


list=[0,1,2,3,4,5,6,7]
item=6
result=binary_search(list,0,len(list)-1,item)

if result!=None:
    print(result)
else:
	print('Not Found !')
'''
 Binary Search using Recursion
 Assume that list is already in Ascending order.

 Space Complexity of Binary Search using Recursion is more than simple Binary Search 
 Becuase it make use of Recursion Stack for each function call
'''



def binary_search(list,lower,upper,item):
	''' 
	Funtion for binary search of element in list 
	Synatx: binary_search( list,lower,upper,item)
	Return index of element where the item is found
	Time Complexity: O(logn) 
	Space Complexity: O(logn)
	Recurence Relation : T(n)=T(n/2)+C  (C represents constant) 
	'''
	if lower<=upper:
		middle=(lower+upper)//2 #finding middle element index

		#if item is mathched with middle element then middle is the required index
		if list[middle]==item:
			return middle

		#if item is greater than the middle element then apply Binary Search on right portion of list
		elif list[middle]<item:
			return  binary_search(list,middle+1,upper,item)

		#if item is greater than the middle element then apply Binary Search on left portion of list
		else:
			return binary_search(list,lower,middle-1,item)	


list=[0,1,2,3,4,5,6,7]
item=6
result=binary_search(list,0,len(list)-1,item)

if result!=None:
    print(result)
else:
	print('Not Found !')
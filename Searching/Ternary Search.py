'''
 Ternary Search on lists
 Assume that list is already in Ascending order.

 The no of Recursive Calls for Ternary Search is less than Binary Search
'''



def ternary_search(list,lower,middle,upper,item):
	''' 
	    funtion for binary search of element in list 
	    synatx: ternary_search(list,lower,middle,upper,item)
	    return index of element where the item is found
	    Time Complexity: O(logn) 
	    Space Complexity: O(logn) 
	'''
	if lower<=middle and middle<=upper:
	    left_middle=(lower+middle)//2 #finding middle element index of left list
	    right_middle=(middle+upper)//2 #finding middle element index of right list

	    #if item is mathched with left_middle element
	    if list[left_middle]==item :
	    	return left_middle

	    #if item is mathched with middle element	
	    elif list[middle]==item:
	    	return middle

	    #if item is mathched with right_middle element	
	    elif list[right_middle]==item:
	    	return right_middle

        #if item is less than the left_middle element 
	    elif list[left_middle]>item:
		    return  ternary_search(list,lower,(lower+left_middle)//2,left_middle-1,item)

        #if item is between than the left_middle and middle 
	    elif list[left_middle]<item and item<list[middle]:
		    return  ternary_search(list,left_middle+1,(left_middle+middle)//2,middle-1,item)

        #if item is between than the middle and right_middle 
	    elif list[middle]<item and item<list[right_middle]:
		    return  ternary_search(list,middle+1,(middle+right_middle)//2,right_middle-1,item)

        #if item is greater than the right_middle
	    elif list[right_middle]<item :
		    return  ternary_search(list,right_middle+1,(right_middle+1+upper)//2,upper,item)


list=[0,1,2,3,4,5,6,7]
item=7
result=ternary_search(list,0,(len(list)-1)//2,len(list)-1,item)

if result!=None:
    print(result)
else:
	print('Not Found !')
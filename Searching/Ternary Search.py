'''
 Ternary Search on lists
 Assume that list is already in Ascending order.

 The number of Recursive Calls and Recisrion Stack Depth is lesser for Ternary Search as compared to Binary Search
'''



def ternary_search(list,lower,upper,item):
	''' 
	    funtion for binary search of element in list 
	    synatx: ternary_search(list,lower,upper,item)
	    return index of element where the item is found
	    Time Complexity: O(logn) 
	    Space Complexity: O(logn) 
	'''
	if lower<=upper:
	    first_middle=lower+((upper-lower)//3) #finding 1st middle element which is at (n/3)rd index of list
	    second_middle=lower+(((upper-lower)*2)//3) #finding 2nd middle element which is at (2n/3)rd index of list

	    #if item is mathched with first_middle element then first_middle is the required index
	    if list[first_middle]==item :
	    	return first_middle

	    #if item is mathched with second_middle element	then second_middle is the required index
	    elif list[second_middle]==item:
	    	return second_middle


        #if item is less than the first_middle element then apply Ternary Search on Left portion of list
	    elif list[first_middle]>item:
		    return  ternary_search(list,lower,first_middle-1,item)

        #if item is between than the first_middle and second_middle then apply Ternary Search on Middle portion of list
	    elif list[first_middle]<item and item<list[second_middle]:    	
		    return  ternary_search(list,first_middle+1,second_middle-1,item)

        #if item is greater than the second_middle then apply Ternary Search on Right portion of list
	    elif list[second_middle]<item :
		    return  ternary_search(list,second_middle+1,upper,item)


list=[0,1,2,3,4,5,6,7]
item=5
result=ternary_search(list,0,len(list)-1,item)

if result!=None:
    print(result)
else:
	print('Not Found !')
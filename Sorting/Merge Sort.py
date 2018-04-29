'''
 SORT the given array using Merge Sort
 
Conceptually, a Merge sort works as follows:
1.Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
2.Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
 '''


def merge_sort(list):
	''' 
	Funtion to sort the list using Merge Sort
	Syntax: merge_sort(list)
	Time Complexity: O(nlogn)
	Recurence Relation : T(n)=2T(n/2)+O(n) 
	'''
	if len(list)>1:
		mid=len(list)//2 #compute the middle element index 
		left_list=list[:mid]
		right_list=list[mid:]
		#Recursively sort the remaining left and right sublists
		merge_sort(left_list)
		merge_sort(right_list)
		#Merge the sorted left_list and right_list into list
		merge(left_list,right_list,list)


def merge(left_list,right_list,merged_list):
	''' 
	Funtion to merge the sorted left_list and right_list into merged_list
	Syntax:  merge(left_list,right_list,merged_list)
	Time Complexity: O(nlogn)
	Recurence Relation : T(n)=2T(n/2)+O(n) 
	'''
	l=0 #left-list pointer
	r=0 #right-list pointer
	k=0 #merged-list pointer
    
    #while there are some elements in both the left_list and the right_list
	while l< len(left_list) and r< len(right_list):
		#compare there element and add the smaller element to the merged_list
		if left_list[l]<right_list[r]:
			merged_list[k]=left_list[l]
			l+=1
		else:
			merged_list[k]=right_list[r]
			r+=1
		k+=1	
	
	#if some element are remaining in the left_list then simply add them to the merged_list		
	while l< len(left_list):
		merged_list[k]=left_list[l]
		l+=1
		k+=1

	#if some element are remaining in the right_list then simply add them to the merged_list	
	while r< len(right_list):
		merged_list[k]=right_list[r]
		r+=1
		k+=1
	


list=[6,10,13,5,8,3,2,11]
merge_sort(list)
print(list)
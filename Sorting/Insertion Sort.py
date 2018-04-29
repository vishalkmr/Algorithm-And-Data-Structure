'''
 SORT the given array using Insertion Sort
 
 Example:
 let the initial array is  [3, 6, 1, 8, 5, 2, 4, 7]   
 [3, 6, 1, 8, 5, 2, 4, 7]
 [3, 6, 1, 8, 5, 2, 4, 7]
 [1, 3, 6, 8, 5, 2, 4, 7]
 [1, 3, 6, 8, 5, 2, 4, 7]
 [1, 3, 5, 6, 8, 2, 4, 7]
 [1, 2, 3, 5, 6, 8, 4, 7]
 [1, 2, 3, 4, 5, 6, 8, 7]
 [1, 2, 3, 4, 5, 6, 7, 8]
 [1, 2, 3, 4, 5, 6, 7, 8]
'''


def insertion_sort(list):
	''' 
	Funtion to sort the list using Insertion Sort
	Syntax: insertion_sort(list)
	Time Complexity:
	 Worst Case : O(n^2) 
	 Best Case : O(n)   
	'''   
	for index in range(len(list)):
		current_element=list[index]
		position=index

		#now sublist list[0,(index-1)] is already sorted
		#Now we have to insert the current_element in the list such that list remains sorted
		while position and current_element<list[position-1]:
			list[position]=list[position-1]
			position-=1
		list[position]=current_element


list=[3,6,1,8,5,2,4,7]
insertion_sort(list)
print(list)
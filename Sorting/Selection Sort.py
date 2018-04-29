'''
 SORT the given array using Selection Sort
 
 Example:  
 3 6 1 8 5 2 4 7 // this is the initial, starting state of the array

 3 6 1 8 5 2 4 7 // select the mininmum and append it to the already sorted sublist (beggining of the list). hence list =[1, 6, 3, 8, 5, 2, 4, 7] 

 1 6 3 8 5 2 4 7 // select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 8, 5, 6, 4, 7]

 1 2 3 8 5 6 4 7 //  select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 8, 5, 6, 4, 7]

 1 2 3 8 5 6 4 7 //  select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 4, 5, 6, 8, 7]

 1 2 3 4 5 6 8 7 //  select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 4, 5, 6, 8, 7]

 1 2 3 4 5 6 8 7 //  select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 4, 5, 6, 8, 7]

 1 2 3 4 5 6 8 7 //  select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 4, 5, 6, 7, 8]

 1 2 3 4 5 6 8 7 //  select the mininmum in the remaining list and append it to the already sorted sublist. hence list =[1, 2, 3, 4, 5, 6, 7, 8]
 
'''


def selection_sort(list):
	''' 
	Funtion to sort the list using Selection Sort
	Syntax: selection_sort(list)
	Time Complexity:
     Worst Case : O(n^2) 
     Best Case : O(n) 
	'''
	for index in range(len(list)):
		minimum=index
		#find the minimum element index in list[index,(N-1)]
		for position in range(index,len(list)):
			if list[minimum]>list[position]:
				minimum=position
		#append the (index+1)th minimum indexed element on already sorted list
		#here sublist list[0,index-1] is already sorted
		list[index],list[minimum]=list[minimum],list[index]



list=[3,6,1,8,5,2,4,7]
selection_sort(list)
print(list)
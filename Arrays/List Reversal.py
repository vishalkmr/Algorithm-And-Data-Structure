'''
 Reverse the given list items

 Example
 reverse([1,2,3,4,5,6,7])
 Returns:[7, 6, 5, 4, 3, 2, 1]
'''

def reverse(list):
	''' 
	Funtion to reverse list items
	Syntax: reverse(list)
	Time Complexity: O(n)  	
	'''
	length=len(list)-1
	current=0
	#swaping 1st and last elements at each iteration
	while current<length-current:
		list[current],list[length-current]=list[length-current],list[current]
		current+=1

		

list=[1,2,3,4,5,6,7]
reverse(list)
print(list)
'''
 Find the maximum and minimum element in the given list 

 Example
 max_min([11,-2,3,6,14,8,16,10])
 Returns: (-2, 16)
'''

def max_min(list):
	''' 
	Funtion to return maximum and minimum element in the given list 
	Syntax: max_min(list)
	Time Complexity: O(n)  	
	'''
	maximum=list[0] #stores the maximum element in the list
	minimum=list[0] #stores the minimum element in the list

	for element in list:

		#if current element is greater than maximum then make the current element as the maximum element
		if element >maximum:
			maximum=element

		#if current element is lesser than minimum then make the current element as the minimum element
		if element < minimum:
			minimum=element

	return (minimum,maximum)


		
list=[11,-2,3,6,14,8,16,10]

result=max_min(list)
print(result)
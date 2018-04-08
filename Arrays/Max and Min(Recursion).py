'''
 Find the maximum and minimum element in the given list using Recursion

 Example
 max_min([11,-2,3,6,14,8,16,10])
 Returns: (-2, 16)
'''

def max_min(list,index,minimum,maximum):
	''' 
	Funtion to return maximum and minimum element in the given list 
	Syntax: max_min(list,index,minimum,maximum)
	Time Complexity: O(n)  	
	Space Complexity: O(n)
	Recurence Relation : T(n)=T(n-1)+C  (C represents constant) 	
	'''

	if index <len(list):

		#if current element is lesser than minimum then make the current element as the minimum element
		if list[index]<minimum:
			minimum=list[index]

		#if current element is greater than maximum then make the current element as the maximum element	
		if list[index]>maximum:
			maximum=list[index]

		#recursively compute the maximum and minimum element of the remaining list
		return max_min(list,index+1,minimum,maximum)
		
	#if all element of list are encountered	
	#return the current  maximum and minimum element
	else :
		return (minimum ,maximum)

		
list=[11,-2,3,6,14,8,16,10]

minimum=9999
maximum=-9999
result=max_min(list,0,minimum,maximum)
print(result)
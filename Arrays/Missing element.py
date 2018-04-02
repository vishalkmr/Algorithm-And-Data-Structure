'''
 Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array 
 and deleting a random element. Given these two arrays, find which element is missing in the second array.

 Example :
 The first array is shuffled and the number 5 is removed to construct the second array then
 missing_element([1,2,3,4,5,6,7],[3,7,2,1,4,6])
 Returns: 5
'''	

#using Soting
def missing_element(arr1,arr2):
	''' 
	Funtion return missing element
	Syntax: missing_element(arr1,arr2)
    Time Complexity: O(nlogn)  	
	'''	
	# Sort the arrays
	arr1.sort()
	arr2.sort()

	# Compare elements in the sorted arrays
	for num1, num2 in zip(arr1,arr2):
		if num1!= num2:
			return num1


#using Dictionary
def missing_element1(arr1,arr2):
	''' 
	Funtion return missing element
	Syntax: missing_element(arr1,arr2)
    Time Complexity: O(n)  	
	'''
	count={}

	#Storing the element count of array2 in Dictionary
	for i in arr2:
		if i in count:
			count[i]+=1
		else:
			count[i]=1

	#Compairing the elements count in array1 with Dictionary		
	for i in arr1:
		if i not  in count:
			return i		
		elif count[i]==0:
			return i
		else:
			count[i]-=1	
		

#using EXOR-Logic
def missing_element(arr1,arr2):
	''' 
	Funtion return missing element
	Syntax: missing_element(arr1,arr2)
	Time Complexity: O(n)  	
	'''	 
	result=0 

	# Perform an XOR between the numbers in the concatnated arrays (arr1+arr2)
	for num in arr1+arr2: 
		result^=num 

	return result 




arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]

output=missing_element1(arr1,arr2)
print(output)
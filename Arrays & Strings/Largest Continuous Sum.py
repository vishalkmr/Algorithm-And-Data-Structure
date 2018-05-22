'''
Given an array of integers (positive and negative) 
Find the largest continuous sum ,along with starting and end point of largest continuous sum

Example
largest_continuous_sum([1,-3,6,-2,4,-2,9,-10,5])
Returns: (15, 2, 6)

i.e the subrange [6,-2,4,-2,9] gives the largest sum
	which is equal to 15 and it starts from index 2 and ends at index 6 
'''


def largest_continuous_sum(arr):
	''' 
	Funtion return the largest continuous sum of array
	Syntax: largest_continuous_sum(arr)
	Time Complexity: O(n)  	
	'''	 
    # Check to see if array is length 0
	if len(arr)==0: 
		return 0
    
	# max_sum contains overall maximum sum
	# current_sum contains max sum upto the current element
	max_sum=current_sum=arr[0] 
		
	start=0 #start points to starting point of largest continuous sum
	end=0 #end points to end point of largest continuous sum
	index=0 #index points to current index of array
		
	# For every element in array from 1st index
	for num in arr[1:]:
		
		#incrementing the index
		index+=1 
		
		# Set current_sum as the higher of the two
		current_sum=max(current_sum+num, num)

		#if current_sum is equal to num means new sum sequence is started
		if current_sum==num:
			start=index
		
		# Set max_sum as the higher between the current_sum and the max_sum
		max_sum=max(current_sum, max_sum) 
		
		#if max_sum is equal to current_sum means the sum sequence is stoped
		if max_sum==current_sum:
			end=index

	return max_sum,start,end



arr = [1,-3,6,-2,4,-2,9,-10,5]
output=largest_continuous_sum(arr)
print(output)
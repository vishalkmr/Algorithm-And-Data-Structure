'''
Given a string, find the longest substring without repeating characters

Example
largest_non_repeat('abcdabcbb')
Returns: 'abcd'
'''

def largest_non_repeat(string):
	''' 
	Funtion return the longest substring without repeating characters in the given string
	Syntax: largest_non_repeat(string)
	'''	 
	longest_substring=''
	substring=''

	for letter in string:

		#if letter is already in substring means the letter is repated
		if letter in substring:
			#compare the substring with longest_substring 
			#if substring is larger than the longest_substring 
			if len(substring)>len(longest_substring):
				longest_substring=substring #then update the longest_substring
			
			#update the substring
			substring=letter 

		#if letter is not in substring 
		#means no repeatation
		else:
			substring=substring+letter #append the letter onto substring
	
	return longest_substring		



string = 'abcdabcbb'
output=largest_non_repeat(string)
print(output)

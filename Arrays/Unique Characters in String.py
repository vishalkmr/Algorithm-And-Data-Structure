''' 
 Given a string,determine if it is compreised of all unique characters.
 For example, the string 'abcde' has all unique characters and should return True. 
 The string 'aabcde' contains duplicate characters and should return false.
 
 Assume that the sollution is case sensitive i.e. string 'ABBabb' retruns True

 Example
 compression('abcdefg')
 Returns: True
'''

#using Set
def unique_characters(string):
	''' 
	Funtion to determine if the given string is compreised of all unique characters
	Syntax: insert(string)
	retruns True if all characters are unique	
	Time Complexity: O(n)  	
	'''
	#if string contains all unique characters 
	#Then the number of letters in string must be equal to number of elements present in set constructed from that string
	#Because set contails only unique elements
	return	len(string) == len(set(string))


#usng Dictionary	
def unique_characters(string):
	''' 
	Funtion to determine if the given string is compreised of all unique characters
	Syntax: insert(string)
	retruns True if all characters are unique	
	Time Complexity: O(n)  	
	'''
	count={} #creating a count dictionary 

	for letter in string:

		#if letter is already present in count dictionary means that letter appears more than once
		#hence retrun false
		if letter in count:
			return False
		#if letter is not present in count dictionary then add it in the dictionary
		else:
			count[letter]=1

	return 	True






	
string='abcdefg'

result=unique_characters(string)
print(result)

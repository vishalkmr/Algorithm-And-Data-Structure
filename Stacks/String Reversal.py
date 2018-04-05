'''
 Reverse the given string using Stack

 Example
 reverse('dog')
 Returns: 'god'
'''

from Stack import Stack

def reverse(string):
	''' 
	Funtion to reverse string
	Syntax: reverse(string)
	Time Complexity: O(n)  	
	'''	
	stack=Stack() #creating a stack object
	output='' #stores the reverse string

	for letter in string:
		stack.push(letter) #Pusing the letter of string into stack

	for item in stack:
		output=output+str(stack.pop())	#Poping the stack item and appending to output string

	return output


		
string='dog'

output=reverse(string)
print(output)	
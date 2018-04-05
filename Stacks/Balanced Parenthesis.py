"""
 Given a expression containing  simple mathematics along with parenthesis
 determine if the input expression contains balanced parenthesis

 Example
 balanced('(a+b)/(c+d(e-f))')
 Returns: True
"""

from Stack import Stack

def balanced(expression):
	''' 
	Funtion returns True if given expression contains balanced parenthesis
	Syntax: reverse(string)
	Time Complexity: O(n)  	
	'''	
	stack=Stack() #creating a stack object

	for element in expression:
		#if left paranthesis appears then push that onto stack
		if element=='(':
			stack.push(element)
		
		#if right parenthesis appears
		elif element==')':
			try:
				#then pop the elements from operator_stack until we get the (
				temp = stack.pop()			
				while (temp is not '('):
					postfix_expression = postfix_expression + temp
					temp = stack.pop()

			#exception may genrate while poping from empty stack
			except:
				return False	

	#finally if no element present in stack means parenthesis are balanced in the given expression			
	if len(stack)==0:
		return True
	else:
		return False			




expression='(a+b)/(c+d(e-f))'

result=balanced(expression)
print(result)
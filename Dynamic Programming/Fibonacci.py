''' 
	Program to return nth fibonacci number
	The Fibonacci numbers are the numbers in the following integer sequence.
		0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

	In mathematical terms, the sequence F(n) of Fibonacci numbers is defined by the recurrence relation
	    F(n) = F(n-1) + F(n-2)
'''


#Conventional Recursive Method
def fibonacci(n):
	''' 
	Funtion return nth fibonacci number
	Syntax:fibonacci(n)
	Time Complexity: O(2^n)  	
	'''	
	if n==0 or n==1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)


#Using Dynamic Programming
def fibonacci(n):
	''' 
	Funtion return nth fibonacci number
	Syntax:fibonacci(n)
	Time Complexity: O(n)  	
	'''	
	if n==0 or n==1:
		memory[n]=n
		return n
	else:
		if memory[n-1] is None:
			memory[n-1]=fibonacci(n-1)
		if memory[n-2] is None:
			memory[n-2]=fibonacci(n-2)

		memory[n]=memory[n-1]+memory[n-2]	
		return memory[n]

n=7
memory=[None]*(n+1)

result=fibonacci(n)
print(result)

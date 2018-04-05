''' 
	Program to print fibonacci series
	The Fibonacci numbers are the numbers in the following integer sequence.
		0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

	In mathematical terms, the sequence F(n) of Fibonacci numbers is defined by the recurrence relation
	    F(n) = F(n-1) + F(n-2)
'''
def fibonacci(n):	
	a,b=0,1
	for i in range(n): #Time Complexity: O(n) 
		print(b)
		a,b=b,a+b

fibonacci(10)
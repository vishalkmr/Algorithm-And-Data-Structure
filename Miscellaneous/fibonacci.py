''' 
	Program to print fibonacci series
	The Fibonacci numbers are the numbers in the following integer sequence.
		0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

	In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
	    Fn = Fn-1 + Fn-2
'''

loop_counter=12
a,b=0,1
for i in range(loop_counter): #Time Complexity: O(n) 
	print(b)
	a,b=b,a+b

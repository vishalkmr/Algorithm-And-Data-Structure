''' 
 Program to calculate the Factorial of given number

 In mathematical terms, factorial of nth nuber is defined by following relation
    F(n)=n*(n-1)*(n-2)*......1
    F(n)=n*F(n-1)
'''

#using Iterations
def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact	

#using Recusion
def factorial(n):
	#terminating condition
	if n==1: 
		return 1
	else:
		return n*factorial(n-1)

result=factorial(5)
print(result)
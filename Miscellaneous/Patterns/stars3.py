"""
    program to print the pattern
	    *
	   ***
	  *****
	 *******
	*********
	n=5
"""

n=int(input("enter the number : "))
#initialization of variable
space=n-1
stars=1
i=0
#loop for executes the code n times
for i in range(0,n):
    #loop print spaces
	for i in range(0,space): 
		print(" ",end='')
	#loop print stars	
	for i in range(0,stars):  
		print("*",end='')
    #upadation in the values of stars and space
	stars=stars+2
	space=space-1
	#to print new line
	print()

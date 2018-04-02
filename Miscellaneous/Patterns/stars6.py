"""
    program to print the pattern
	    *		 *	
	   ***		***
	  *****    *****
	 *******  *******
	******************
	n=5
"""

n=int(input("enter the number : "))
#initialization of variable
space1=n-1
space2=2*n-2
stars=1
i=0
#loop for executes the code n times
for i in range(0,n):
    #loop print spaces1
	for i in range(0,space1): 
		print(" ",end='')
	#loop print stars	
	for i in range(0,stars):  
		print("*",end='')
    #loop print spaces2
	for i in range(0,space2): 
		print(" ",end='')
	#loop print stars	
	for i in range(0,stars):  
		print("*",end='')
    
	
	#upadation in the values of stars and space
	stars=stars+2
	space1=space1-1
	space2=space2-2
	
	#to print new line
	print()

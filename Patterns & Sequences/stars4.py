"""
    program to print the pattern
	*********	    
	 *******		
	  *****		
	   ***	
            *

	n=5
"""

#taking input
n=int(input("enter the number : "))

#initialization of variable
space=0
stars=2*n-1

#loop for n lines
for i in range(0,n):
    #loop to print spaces
	for i in range(0,space): 
		print(" ",end='')

	#loop to print stars	
	for i in range(0,stars):  
		print("*",end='')

    #upadation in the values of stars and space
	stars=stars-2
	space=space+1

	#to print new line
	print()

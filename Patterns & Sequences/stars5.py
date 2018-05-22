"""
    program to print the pattern
	    *
	   ***
	  *****
	 *******
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
space=n-1
stars=1
sign=1

#loop for 2n-1 lines
for i in range(0,2*n-1):
    #loop to print spaces
	for i in range(0,space): 
		print(" ",end='')
	
	#loop to print stars	
	for i in range(0,stars):  
		print("*",end='')

	#toggle the sign
	if stars==(2*n-1):
		sign=-1

    #upadation in the values of stars and space
	stars=stars+2*sign
	space=space-1*sign
	
	#to print new line
	print()


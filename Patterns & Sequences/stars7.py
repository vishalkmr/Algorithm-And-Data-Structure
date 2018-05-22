"""
    program to print the pattern
		*
	   * *
	  *   *
	 *     *
	*       *
	 *     *		
	  *   *		
	   * *	
		*

	n=5
"""

#taking input
n=int(input("enter the number : "))

#initialization of variable
space1=n-1
space2=-1
sign=1

#loop for 2n-1 lines
for i in range(0,2*n-1):
    #loop to print spaces1
	for i in range(0,space1): 
		print(" ",end='')
	
	#print stars	
	print("*",end='')
	
	if(space2!=-1):		
		#loop to print spaces2
		for i in range(0,space2): 
			print(" ",end='')

		#print stars	
		print("*",end='')

	#toggle the sign
	if space1==0:
		sign=-1

	#upadation in the values of spaces
	space1=space1-1*sign
	space2=space2+2*sign

	#to print new line
	print()

"""
    program to print the pattern
	*
	**
	***
	****
	*****
	n=5
"""

#taking input
n=int(input("enter the number : "))

#initialization of variable
stars=1

#loop for n lines
for i in range(0,n):
    #loop to print stars	
	for i in range(0,stars):  
		print("*",end='')
   
    #upadation in the values of stars 
	stars=stars+1
	
	#to print new line
	print()

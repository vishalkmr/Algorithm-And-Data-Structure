"""
    program to print the pattern
	*
	**
	***
	****
	*****
	n=5
"""

n=int(input("enter the number : "))
#initialization of variable

stars=1
i=0
#loop for executes the code n times
for i in range(0,n):
    #loop print stars	
	for i in range(0,stars):  
		print("*",end='')
    #upadation in the values of stars and space
	stars=stars+1
	#to print new line
	print()

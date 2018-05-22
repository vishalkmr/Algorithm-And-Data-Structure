"""
  Program to print the pattern
	
	 x   	n=1

	+x+
	xxx		n=3    
	+x+	

	++x++
	+xxx+		    
	xxxxx   n=5
	+xxx+
	++x++

 Assume n to be odd.
"""

#taking input
n=int(input("enter the number : "))

#initialization of variable
plus=int((n-1)/2)
x=1
sign=1

#loop for n lines
for i in range(0,n):
    #loop to print plus 
	for j in range(0,plus): 
		print("+",end='')
	
	#print x
	for k in range(0,x): 	
		print("x",end='')
	
	#loop to print plus
	for l in range(0,plus): 
		print("+",end='')
	
	#toggle the sign
	if x==n:
		sign=-1

	#updation of variable
	x=x+2*sign
	plus=plus-1*sign
	
	#to print new line
	print()

	
	
 
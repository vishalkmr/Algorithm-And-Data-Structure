''' 

'''


#Conventional Recursive Method
def longet_common_subseqeuence(x,y,n,m):
	''' 
	Funtion return the length of longest subseqeuence between string x and y
	Syntax:longet_common_subseqeuence(x,y,n,m)
	Time Complexity: O(2^(n+m))  	
	'''	

	if n<0 or m<0:
		return 0
	else:	
		if x[n]==y[m]:
			return 1+longet_common_subseqeuence(x,y,n-1,m-1)
		else:
			a=longet_common_subseqeuence(x,y,n-1,m)
			b=longet_common_subseqeuence(x,y,n,m-1)	
			return max(a,b)

#Using Dynamic Programming
def longet_common_subseqeuence(x,y,n,m):
	''' 
	Funtion return the length of longest subseqeuence between string x and y
	Syntax:longet_common_subseqeuence(x,y,n,m)
	Time Complexity: O(n.m)
	'''	
	if n<0 or m<0:
		return 0
	else:	
		if x[n]==y[m]:
			if memory[n-1][m-1] is None:
				memory[n-1][m-1]=longet_common_subseqeuence(x,y,n-1,m-1)
			memory[n][m]=1+memory[n-1][m-1]
			return memory[n][m]
		else:
			if memory[n-1][m] is None:
				memory[n-1][m]=longet_common_subseqeuence(x,y,n-1,m)
			if memory[n][m-1] is None:
				memory[n][m-1]=longet_common_subseqeuence(x,y,n,m-1)
			
			memory[n][m]=max(memory[n-1][m],memory[n][m-1])
			return memory[n][m]




x='vishal@123'
y='vigggghhhassl'
n=len(x)-1
m=len(y)-1


#Memory Matrix (n X m) for Dynamic Programming
memory=[[None for i in range(m+1)] for j in range(n+1)]
result=longet_common_subseqeuence(x,y,n,m)
print(result) 
print(memory)
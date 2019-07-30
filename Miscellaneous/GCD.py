''' 
Find the greatest common divisor (gcd) of two integer.
GCD is the largest positive integer that divides each of the integers. 
For example, the gcd of 8 and 12 is 4.
'''

def gcd(m,n):
	#m.n
	#find prime factors of m
	m_prime_factor=[]
	for i in range(1,m+1):
		if(m%i==0):
			m_prime_factor.append(i)

	#find prime factors of n
	n_prime_factor=[]
	for j in range(1,n+1):
		if(n%j==0):
			n_prime_factor.append(j)
	
	#find prime factors common for m and n
	common_prime_factor=[]
	for factor in m_prime_factor:
		if factor in n_prime_factor:
			common_prime_factor.append(factor)

	#return the largest common prime factor
	return(common_prime_factor[-1])		

def gcd(m,n):
	#min(m.n)
	#find prime factors common for m and n
	common_prime_factor=[]
	for i in range(1,min(m,n)+1):
		if(m%i==0) and (n%i==0) :
			common_prime_factor.append(i)
	
	#return the largest common prime factor
	return(common_prime_factor[-1])		



def gcd(m,n):
	#min(m.n)
	
	#find prime factors common for m and n
	for i in range(1,min(m,n)+1):
		if(m%i==0) and (n%i==0) :
			common_prime_factor=i

	return common_prime_factor		


def gcd(m,n):
	#min(m.n)
	i=min(m,n)
	#end to begining
	while i>0:
		if(m%i==0) and (n%i==0) :
			return i
		
		i=i-1
		

def gcd(m,n):
#logn
	if n==0:
		return m
	if m==1 :
		return 1
	return gcd(n,m%n)



result=gcd(4,2)
print(result)

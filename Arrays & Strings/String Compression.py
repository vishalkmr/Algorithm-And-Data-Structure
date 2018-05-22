''' 
 Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
 
 Assume yhe result is case sensitive, so that a string 'AAAaaa' returns 'A3a3'	
 
 Example
 compression('AAABBBBBBBBBCCCCCCCCDDDDDDD')
 Returns: 'A3B9C8D7'
'''


def compression(string):
	''' 
	Funtion to compress the given string
	Syntax: insert(string)
	Returns the compressed string
	Time Complexity: O(n)  	
	'''
	temp=string[0]	#to store the letter temporarily until its is processed
	count=0 #to count the number of occurence of the temporary_letter in the given string
	output='' #stores the comressed string

	for letter in string:

		#if letter is same as the temporary_letter
		#That  letter is still present in the string and hence increase its count
		if letter==temp:
			count+=1

		#if letter is different than the temporary_letter
		#That means new letter is apeared 
		else:
			output=output+temp+str(count) #so we store the temporary_letter along with its count into the compressed output string 
			temp=letter #update temporary_letter with the new variable value
			count=1 #initialize count for new temporary_letter as 1

	#for accomodation of last letter
	output=output+temp+str(count)	

	return output			



	
string='AAABBBBBBBBBCCCCCCCCDDDDDDD'


output=compression(string)
print(output)

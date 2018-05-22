'''
 Given two strings, check to see if they are Anagrams. 
 An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
 Means two strings are said to be anagrams if they are written using the exact same letters 

 Example
 anagram('Anagram','Naga Ram')
 Returns: True
'''

#using Sorting
def anagram(string1,string2):
	''' 
	Funtion return True if strings are Anagrams
	Syntax: insert(string1,string2)
	Time Complexity: O(nlogn)  	
	'''
	#Removing the spaces and Converting the strings in lowercase
	string1=string1.replace(' ','').lower()
	string2=string2.replace(' ','').lower()
	
	#Compairing the sorted string letters one to one
	return sorted(string1) == sorted(string2)


#usng Dictionary	
def anagram(string1,string2):
	''' 
	Funtion return True if strings are Anagrams
	Syntax: insert(string1,string2)
	Time Complexity: O(n)  	
	'''
	#Removing the spaces and Converting the strings in lowercase
	string1=string1.replace(' ','').lower()
	string2=string2.replace(' ','').lower()
	
	if len(string1)!=len(string2):
		return False

	count={} #creating a count dictionary 

	#Storing the counts of letters of string1 into count dictionary
	for letter in string1:
		if letter in count:
			count[letter]+=1
		else:
			count[letter]=1
	
	#Removing the letter count from dictionary if letter is present in the in string2
	for letter in string2:
		if letter in count:
			count[letter]-=1
		else:
			count[letter]=1
		
	#If count[letter] is 0 means same letter appear same number of times in both strings
	#Otherwise it means letters did not appear similar numbers of time in strings
	for letter in count:
		if count[letter]!=0:
			return False
	return True



	
string1='Anagram'
string2='Naga Ram'

if anagram(string1,string2):
	print('Yes Strings are Anagram')
else:
	print('No Strings are not Anagram')
	
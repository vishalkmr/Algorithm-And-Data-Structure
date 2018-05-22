'''
Given a string of words ( known as Sentence ),reverse all the words.

Example
reverse('name is vishal kumar')
Returns: 'kumar vishal is name'
'''

#using soting
def reverse(sentence):
	''' 
	Funtion to reverse all the words in given sentence
	Syntax: reverse(sentence)
	Time Complexity: O(nlogn)  	
	'''
	#1st spliting the sentence into word list i.e. ['name', 'is', 'vishal', 'kumar']
	#then sort the word list in reverse order i.e. ['kumar', 'vishal', 'is', 'name']
	#joining the revresed list back into string
	return ' '.join(sentence.split()[::-1]) 


#using Parsing
def reverse(sentence):		
	''' 
	Funtion to reverse all the words in given sentence
	Syntax: reverse(sentence)
	Time Complexity: O(n)  	
	'''
	i=len(sentence)-1
	reverse_word_list=[] #contains the reversed sentence
	word_length=0
	word=''
	
	#parsing the string from last
	while i >=0 :

		if sentence[i]==' ':
			#if space is encountered and word_length is not zero 0
			#means a new word is formed 
			if word_length!=0:
				reverse_word_list.append(word)
				word=''
				word_length=0		
		else:
			#if i is some regular letter in the word of the sentence
			#then concatinate the letter with current word
			word=sentence[i]+word
			word_length+=1  #increment the word_length
		
		i-=1	#dicrement the loop-counter

	#for accomaodation of 1st letter of the sentence	
	if word_length!=0:
		reverse_word_list.append(word)	

	return ' '.join(reverse_word_list) #joining the revresed word list back into string



		
sentence='name is vishal kumar'
output=reverse(sentence)
print(output)
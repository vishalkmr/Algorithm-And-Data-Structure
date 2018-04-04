'''
 Reverse the given list items (Inplace Algorithm)

 Example
 reverse([1,2,3,4,5,6,7])
 Returns:[7, 6, 5, 4, 3, 2, 1]
'''

def reverse(list):
	''' 
	Funtion to reverse list items
	Syntax: reverse(list)
	Time Complexity: O(n)  	
	'''
	length=len(list)-1
	beg=0 #pointing to begining of the list
	end=length #pointing to ending of the list
	
	while beg<end:

		#swaping 1st and last elements at each iteration
		list[beg],list[end]=list[end],list[beg]
		
		beg+=1 #incrementing the begining
		end-=1 #dicrementing the ending

		
list=[1,2,3,4,5,6,7]
reverse(list)
print(list)
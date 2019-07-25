'''
Given an integer array, output all the unique pairs that sum up to a specific value k.

Example
pair_sum([1,2,3,4,5,6,7],7)
Returns: (3, 4), (2, 5), (1, 6)
'''
 
#using Sorting
def pair_sum(list,k):
	''' 
	Funtion return all the unique pairs of list elements that sum up to k
	Syntax: insert(list,k)
	Time Complexity: O(nlogn)  	
	'''	
	list.sort() #sorting the list

	length=len(list)
	pairs=[] #for storing the list of pairs that sum up to k
	i=0 #pointing to begining of the list  (Smallest number in the list)
	j=length-1 #pointing to ending of the list (Largest number in the list)

	#making iterations until i and j points to the same element
	while i<=j:		
		
		#if sum of list[i] & list[j] is equal to k that means it is one of the desired pair 
		if list[i]+list[j]==k:
			pairs.append((list[i],list[j]))
			i+=1
			j-=1

		#if these pair sum is less than k
		#we know that the list is sorted and hence j is pointing to Largest number in the list
		#so it is due to value of number pointed by i that is causes there sum to be lesser than k
		#Thus we increment the pointer i so that the sum of values pointed by i and j may gets equal to k
		elif list[i]+list[j]<k:
			i+=1

		#if these pair sum is greater than k
		#we know that the list is sorted and hence i is pointing to Smallest number in the list
		#so it is due to value of number pointed by j that is causes there sum to be greater than k
		#Thus we dicrement the pointer j so that the sum of values pointed by i and j may gets equal to k		
		else:
			j-=1

	return pairs	


#using Set
def pair_sum(list,k):
	''' 
	Funtion return all the unique pairs of list elements that sum up to k
	Syntax: insert(list,k)
	Time Complexity: O(n)  	
	'''
	pairs=[] #for storing the list of pairs that sums up to k
	seen=set() #for storing the elements of the list which are alredy seened

	for current in list:

		target=k-current #stores the desiered value or target value ( which when added to current element of the list yiedls to the sum k )
		
		#if target value is found in the seen set 
		#then the sum of target and list current element is equal to k 
		#Thus we add target & current element touple onto the pairs list
		if target in seen:
			pairs.append((min(target,current),max(target,current))) #formating the pairs touple so like (min_value_of_pairs,max_value_of_pairs)
		
		#if target value is not found in the seen set
		#means the sum of any element of seen set with the current element doesnot yields to k
		#Thus we simply add current element of the list to the seen set in a hop that may be this added_current_element_values can be summed up with upcomming element to produce  k  
		else:
			seen.add(current)
	
	return pairs


list=[1,2,3,4,5,6,7]
pairs=pair_sum(list,7)
print(pairs)

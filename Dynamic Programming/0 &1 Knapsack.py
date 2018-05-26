"""
       0/1 Knapsack
--------------------------------------------
Name  Weight	Profit
--------------------------------------------
obj1	7		80
obj2	6		60
obj3	4		40
--------------------------------------------
		Total Profit : 100
--------------------------------------------
Note : For this example Greedy Approach produces 80 as Total Profit
"""
class Item(object):
	def __init__(self,name=None,weight=None,profit=None):
		self.name=name
		self.weight=weight
		self.profit=profit
		self.composition=0

	def __str__(self):
 		return str(self.name)+'\t'+str(self.weight)+'\t\t'+str(self.profit)+'\t\t'+str(self.composition)



def O1_knapsack(w,n):
	''' 
	Funtion to return maximize profit using 0/1 Knapsack
	Syntax: O1_knapsack(item_list,w,n)    w->weight constraint, n->nth item
	Time Complexity: O(w.n)
	'''
	if w==0 or n==0:
		return 0
	
	#when weight of nth item is more than weight constraint
	#then simply skip that element 
	elif w<item_list[n].weight:
		if memory[w][n-1] is None:
			memory[w][n-1]=O1_knapsack(w,n-1)
	
	#when weight of nth item is less or equal to the weight constraint
	#then consider all possiblities( either take the nth item or skip the nth item)
	#return value which maximize profit	
	else:
		#take the nth item into knapsack
		if memory[w-item_list[n].weight][n-1] is None:
			memory[w-item_list[n].weight][n-1]=O1_knapsack(w-item_list[n].weight,n-1)
			print('asdasdsadas')
		
		#skip the nth item
		if memory[w][n-1] is None:
			memory[w][n-1]=O1_knapsack(w,n-1)
			print('bbbbbbbbbbbbbbbbbbb')
        
        #consider the case which will provide maximum profit
		if memory[w][n] is None:
			print(memory[w-item_list[n].weight][n-1])
			# print(type(memory[w][n-1]))
			if memory[w-item_list[n].weight][n-1]+item_list[n].profit < memory[w][n-1]:
				memory[w][n]=memory[w][n-1]
			else:
				memory[w][n]=memory[w-item_list[n].weight][n-1]+item_list[n].profit
				#if nth item is taken into knapsack then update its composition
				item_list[n].composition=1

		return memory[w][n]
	

item_list=[]

item_list.append(Item('obj1',7,80))
item_list.append(Item('obj2',6,60))
item_list.append(Item('obj3',4,40))

n=2 # max index of items
w=7 # max weight


#Memory Matrix (w X n) for Dynamic Programming
memory=[[None for i in range(n+1)] for j in range(w+2)]

profit=O1_knapsack(w,n)
print(memory)
print("--------------------------------------------")
print('Name  Weight\tProfit\tComposition')
print("--------------------------------------------")
for item in item_list:
	print(item)
print("--------------------------------------------")
print("\t\tTotal Profit : "+str(profit))
print("--------------------------------------------")
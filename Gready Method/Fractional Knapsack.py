import functools

@functools.total_ordering
class Item(object):
	def __init__(self,name=None,weight=None,profit=None):
		self.name=name
		self.weight=weight
		self.profit=profit
		self.pw_ratio=self.profit/self.weight
		self.fraction=None

	def __str__(self):
 		return str(self.name)+'\t'+str(self.weight)+'\t\t'+str(self.profit)+'\t\t'+str(self.pw_ratio)+'\t\t'+str(self.fraction)

	def __lt__(self, other):
		return self.pw_ratio< other.pw_ratio

	def __eq__(self, other):
		return self.pw_ratio == other.pw_ratio

def fractional_knapsack(item_list,max_weight):
	''' 
	Funtion to return maximize profit using Frational Knapsack
	Syntax: fractional_knapsack(item_list,max_weight)
	Time Complexity: O(n.logn)
	'''
	#Sorting items according to P/W ratio
	item_list.sort(reverse=True)
	profit=0

	for item in item_list:
		#if item can fit in knapsack completely then  
		if item.weight<=max_weight: 
			profit+=item.profit #add the item profit to total profit
			max_weight-=item.weight #update the remaining max_weight
			item.fraction=1 #fraction of item taken is 1 (complete)
		
		#if item can not fit in knapsack completely (i.e. item.weight > max_weight) then  
		else:
			item.fraction=max_weight/item.weight #fraction of item taken is given by ratio of (max_weight/item.weight)
			profit+=item.profit*(max_weight/item.weight) #add the item fraction profit to total profit
			max_weight-=item.weight*(max_weight/item.weight) #update the remaining max_weight
	
	return profit		
	


item_list=[]

item_list.append(Item('obj1',10,250))
item_list.append(Item('obj2',5,300))
item_list.append(Item('obj3',12,360))
item_list.append(Item('obj4',8,200))
max_weight=28

profit=fractional_knapsack(item_list,max_weight)

print('Name  Weight\tProfit\tP/W Ratio\tFraction')
for item in item_list:
	print(item)

print(" \t Total Profit : "+str(profit))

'''
 
'''

def hoppable(towers):
	index=0
	while True:

		if index>=len(towers):
			return True

		if towers[index]==0:
			return False

		index=next_step(towers,index)

def next_step(towers,index):
	lb=index+1
	ub=index+towers[index]	
	maximum=towers[lb]
	optimum_step=lb
	for i in range(lb,ub):
		if i>len(towers):
			return i
		if towers[i]>maximum:
			maximum=towers[i]
			optimum_step=i
		print(optimum_step)
	return optimum_step
		
towers=[2,1,5,3,1]

result=hoppable(towers)
print(result)
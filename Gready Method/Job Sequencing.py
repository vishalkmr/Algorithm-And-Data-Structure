import functools

@functools.total_ordering
class Job(object):
	def __init__(self,name=None,profit=None,deadline=None):
		self.name=name
		self.deadline=deadline
		self.profit=profit


	def __str__(self):
 		return str(self.name)+' \t\t '+str(self.profit)+'  \t '+str(self.deadline)

	def __lt__(self, other):
		return self.profit< other.profit

	def __eq__(self, other):
		return self.profit == other.profit

#compute max deadline among the given jobs
def max_deadline(job_list):
	max=0
	for job in 	job_list:
		if job.deadline>max:
			max=job.deadline
	return max


def job_sequencing(job_list):
	''' 
	Funtion to compute profit, panality and left out jobs if job sequencing is done by considering the deadline
	Syntax: job_sequencing(job_list)
	Time Complexity: O(n.logn)
	'''
	#Sorting jobs according to profit
	job_list.sort(reverse=True)
	
	deadline=max_deadline(job_list)
	profit=0
	panality=0
	left_out_jobs=[]

	#creating empty deadline slots
	deadline_list=[None]*(deadline+1)
	
	for job in job_list:
		allocation=True
		
		while allocation:
			#if deadline slot for job is empty then allocate the job
			if deadline_list[job.deadline] is None:
				deadline_list[job.deadline]=job.name
				profit+=job.profit
				allocation=False
			
			#if deadline slot for job is not empty but there may be chance that lower slots are avaliable so update deadline 
			elif job.deadline>1:
				job.deadline-=1
			
			#if job allocation is not possible (no deadline slot is available)
			else:
				allocation=False
				left_out_jobs.append(job.name)
				panality+=job.profit

	return profit,panality,left_out_jobs
 

job_list=[]

#example 1
job_list.append(Job('J1',25,2))
job_list.append(Job('J2',120,1))
job_list.append(Job('J3',50,2))
job_list.append(Job('J4',80,1))

#example 2
# job_list.append(Job('J1',55,5))
# job_list.append(Job('J2',23,2))
# job_list.append(Job('J3',15,4))
# job_list.append(Job('J4',70,1))
# job_list.append(Job('J5',90,3))
# job_list.append(Job('J6',45,2))
# job_list.append(Job('J7',35,1))

print('Name\tProfit\tDeadline')
for job in job_list:
	print(job)

result=job_sequencing(job_list)

print("  Profit : "+str(result[0]))
print("  Panality : "+str(result[1]))
print("  Left Out Jobs : "+str(result[2]))

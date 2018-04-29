# class Job(object):
# 	def __init__(self,name=None,profit=None,deadline=None):
# 		self.name=name
# 		self.deadline=deadline
# 		self.profit=profit


# 	def __str__(self):
#  		return str(self.name)+'  '+str(self.profit)+'  '+str(self.deadline)

# 	def __sortkey__(self):
# 		return self.profit

# 	def __comp__(self,other):
# 		print('comparision')
# 		return cmp(self.profit,other.profit)	



def sort(list):
	''' 
	Funtion to sort the job-list using Selection Sort on the basis of profit
	Syntax: sort(list)
	Time Complexity:
     Worst Case : O(n^2) 
     Best Case : O(n) 
	'''
	for index in range(len(list)):
		maximum=index
		#find the maximum element index in list[index,(N-1)]
		for position in range(index,len(list)):
			if list[maximum].profit<list[position].profit:
				maximum=position
		#append the (index+1)th maximum indexed element on already sorted list
		#here sublist list[0,index-1] is already sorted
		list[index].profit,list[maximum].profit=list[maximum].profit,list[index].profit

def max_deadline(job_list):
	max=0
	for job in 	job_list:
		if job.deadline>max:
			max=job.deadline
	return max


def job_sequencing(job_list):
	deadline=max_deadline(job_list)
	deadline_list=[None]*(deadline+1)
	profit=0
	for job in job_list:
		allocation=True
		i=0
		while allocation:
			if deadline_list[job.deadline] is None:
				print(job.name)
				deadline_list[job.deadline]=job.name
				profit+=job.profit
			elif job.deadline>0:
				pass

	return profit







job_list=[]

job_list.append(['J1',10,20])
job_list.append(['J2',20,2])
job_list.append(['J3',10,3])
job_list.append(['J4',40,3])
job_list.append(['J5',50,2])
job_list.append(['J6',60,1])
for i in range(len(job_list)):
	print(job_list[i])
# sort(job_list)
job_list=job_list[:][1].sort()
print(job_list)
print()
for i in range(len(job_list)):
	print(job_list[i][1])


# profit=job_sequencing(job_list)
# print(profit)
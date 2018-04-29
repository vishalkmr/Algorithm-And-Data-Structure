

# for i in range(len(list)):
# 	small=i

# 	for j in range(i,len(list)):
# 		if list[small]>list[j]:
# 			small=j
# 	temp=list[i]
# 	list[i]=list[small]
# 	list[small]=temp


# for i in range(len(list)):
# 	j=i
# 	while j and list[j]<list[j-1]:
# 		list[j],list[j-1]=list[j-1],list[j]
# 		j=j-1

def mergesort(list,lower,upper):
	if lower<upper:
		mid=(lower+upper)//2
		print(str(lower)+'  '+str(mid)+'  '+str(upper))
		mergesort(list,lower,mid)
		mergesort(list,mid+1,upper)
		merge(list,lower,mid,upper)
		

def merge(list,lower,mid,upper):
	i=lower
	j=mid+1
	result=[]
	while i<=mid and j<=upper:
		if list[i]<list[j]:
			result.append(list[i])
			i=i+1
		else:
			result.append(list[j])
			j=j+1
			
	while i<=mid:
		result.append(list[i])
		i=i+1
		
	while j<=upper:
		result.append(list[j])
		j=j+1
	
	list=result

	
list=[2,4,1,6,7,5,3]
mergesort(list,0,len(list)-1)
print(list)
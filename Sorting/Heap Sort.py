
#under construction...

from math import floor

def max_heapify(list,i):
	left_child=2*i
	right_child=2*i+1

	if  (left_child<=len(list)) and (list[left_child] > list[i]):
		largest=left_child
	else:
		largest=i

	if  (right_child<=len(list)) and (list[right_child] > list[largest]) :
		largest=right_child
	if largest != i:
		list[i],list[largest]=list[largest],list[i]
		max_heapify(list,largest)

	print(list)
		
def buid_heap(list):
	i=floor(len(list)/2-1)
	# 
	while i>0:
		print(i)
		max_heapify(list,i)
		i-=1



list=[3,0,6,1,5,2,4,7]
buid_heap(list)
print(list)
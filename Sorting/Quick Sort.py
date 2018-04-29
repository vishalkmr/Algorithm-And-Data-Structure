'''
 SORT the given array using Quick Sort
 
 Quicksort is a divide and conquer algorithm. Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements. 
 Quicksort can then recursively sort the sub-arrays.

 The steps are:
 1. Pick an element, called a pivot, from the array.
 2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it. 
     After this partitioning, the pivot is in its final position. This is called the partition operation.
 3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
 '''

def quick_sort(list,lb,ub):
    ''' 
    Funtion to sort the list using Quick Sort
    Syntax: quick_sort(list,lb,ub)
    Time Complexity: 
     Worst Case : O(n^2)
     Best Case : O(nlogn)
    Recurence Relation : T(n)=T(n-q)+T(n-p)+O(n) p & q are contants 
     Worst Case :  T(n)=T(c-1)+T(n-c)+O(n)      c is a contant
     Best Case :   T(n)=T(x.n)+T((1/x).n)+O(n)    0<x<1
    '''
    if(lb<ub):
        #Partitioning the list depending on pivot
        pos=partition(list,lb,ub)
        #Recursively sort the remaining left and right sublists    
        quick_sort(list,lb,pos-1)
        quick_sort(list,pos+1,ub)


def partition(list,lb,ub):
    ''' 
    Funtion to partition the list so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it 
    Finally Rerturn the index of pivot
    Syntax: partition(list)
    Time Complexity: O(n)   [Every Case]
    '''
    pivot=list[lb] # initialise pivot
    i=lb #points to element smaller than pivot
    j=ub #points to element larger than pivot

    while(i<=j):
        #from left side of the list find the index whose value is larger than pivot
        while(i<=j and list[i]<=pivot):
            i=i+1
        #from right side of the list find the index whose value is smaller than pivot
        while(i<=j and pivot<list[j]):
            j=j-1
        if(i<j):
            #bring smaller element to the left and larger element to the right side of the list by swapping value pointed by i and j
            list[i],list[j]=list[j],list[i]
    #finally place the pivot at the appropriate position in the list so that left side element are smaller and right side element are larger than pivot value    
    list[lb],list[j]=list[j],list[lb]
    return j


list=[6,10,13,5,8,3,2,11]
quick_sort(list,0,len(list)-1)
print(list)
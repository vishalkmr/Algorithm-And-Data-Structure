'''
 SORT the given array using Bubble Sort
 
 Example:  Let us take the array of numbers "5 1 4 2 8", and sort the array in ascending order using bubble sort. 

 First Pass
 ( 5 1 4 2 8 ) -> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
 ( 1 5 4 2 8 ) -> ( 1 4 5 2 8 ), Swap since 5 > 4
 ( 1 4 5 2 8 ) -> ( 1 4 2 5 8 ), Swap since 5 > 2
 ( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

 Second Pass
 ( 1 4 2 5 8 ) -> ( 1 4 2 5 8 )
 ( 1 4 2 5 8 ) -> ( 1 2 4 5 8 ), Swap since 4 > 2
 ( 1 2 4 5 8 ) -> ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) -> ( 1 2 4 5 8 )
 Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

 Third Pass
 ( 1 2 4 5 8 ) -> ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) -> ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) -> ( 1 2 4 5 8 )
 ( 1 2 4 5 8 ) -> ( 1 2 4 5 8 )

 Simmilarly other Passes yields same Sorted Array.....
'''

#Conventional Bubble Sort
def bubble_sort(list):
    ''' 
    Funtion to sort the list using Bubble Sort
    Syntax: bubble_sort(list)
    Time Complexity: O(n^2)   [Every Case]
    '''
    for elements in list:
        for index in range(len(list)-1):
            #check the adjecent elements are in increasing order or not
            if list[index]>list[index+1]:
                #if not then perform pairwise swaps
                list[index],list[index+1]=list[index+1],list[index] 




#Efficient Bubble Sort
def bubble_sort(list):
    ''' 
    Funtion to sort the list using Bubble Sort
    Syntax: bubble_sort(list)
    Time Complexity:
     Worst Case : O(n^2) 
     Best Case : O(n)   
    '''   
    swapped = True #Flag to monitor that swaping ocuured or not
    while swapped:
        swapped = False
        for index in range(len(list)-1):
            #check the adjecent elements are in increasing order or not
            if list[index] > list[index+1]:
                #if not then perform pairwise swaps
                list[index],list[index+1]=list[index+1],list[index] 
                swapped = True



list=[7, 6, 5, 4, 3, 2, 1]
bubble_sort(list)
print(list)
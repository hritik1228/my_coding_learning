#Selection sort

"""The selection sort algorithm sorts an array by repeatedly finding the minimum 
element (considering ascending order) from unsorted part and putting it at the beginning.
 The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) 
from the unsorted subarray is picked and moved to the sorted subarray."""


# Python program for implementation of Selection 
# Sort 

def selection_sort(array):
    for i in range(len(array)):
        min_arr=i
        for j in range(i+1,len(array)):
            if array[min_arr]>array[j]:
                min_arr=j
                
        array[i],array[min_arr]=array[min_arr],array[i]
    
    return array

A=[23,12,67,22,33,45]

result=selection_sort(A)

print("The sorted result using selection sort is {}".format(result))
        
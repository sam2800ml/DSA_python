
"""
To be able to slice an array the most important is to have an array, then we have to do the following
array[start:stop:step]
whit this we can determine the start point and also the end that we want to grab from that array
"""

import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
slice = arr[2:6] # with this we grab from the third element till the 6
print(slice)

slice2 = arr[:4] # with this we grab all the elements till the 4th element
print(slice2)

slice3 = arr[4:] # with this we grab all the elements after the 4th element
print(slice3)

slice4 = arr[1:9:2] # with this we grab all the elements from the first position till the nine in steps of 2
print(slice4)

"""
Now all the before was for an unidimensional array, but when we have one that is multidimental the slicing changes
array[rows, column]
array[start:stop,start:stop]
the stop is not included
"""

arr2d = np.array([[0,1,2,3],
                  [4,5,6,7],
                  [8,9,10,11],
                  [12,13,14,15]])

slice_2d = arr2d[1:3,1:3]
print(slice_2d)


slice_2d2 = arr2d[2:,2:]
print(slice_2d2)

bool_slicing = arr[arr % 2 == 0]
print(bool_slicing)

con_slicing = arr[(arr > 3) & (arr < 8)]
print(con_slicing)


# array sorting 
"""
Is important to be able to organize data efficiently, arranging the elements in a specific order
the common array sorting algorithms:
- Bubble sort -> compare adjecents elements and swpas them if they are in the wrong order
- Selection sort -> divides an array in to different one sorted and one not, and moves from the unsorted to the sorted
- Insertion sort -> builds the sorted array one element at the time
- Merge sort -> divides the array in two, sorts both of the arrays and then merges it
- Quick sort -> 
- Heap sort
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(i)
        for j in range(0, n-i-1):
            print(j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [2,5,1,7,3]
print(bubble_sort(arr))

def selectiono_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"i {i}")
        min_idx = i
        print(f" min{min_idx}")
        for j in range(i+1, n):
            print(f"j {j}")
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"update min {min_idx}")
        arr[i], arr[ min_idx] = arr[min_idx], arr[i]
    return arr
        
arr = [2,5,1,7,3]
print(selectiono_sort(arr))

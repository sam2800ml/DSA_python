import numpy as np

# the array that we are going to created is 3 rows 4 columns
A = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
)

print(A)
print(A[1,2])

for element in A: # When we do this we print the rows
    for j in element: # if we add the second loop, we iterate each element
        print(j)
"""
We grab the first two rows, and we grab the last 2 columns
"""
subarray = A[:2,-2:] # the first indicates the rows, and the second the column
print(subarray)

# Reshape

"""
Because the array have dimension 3,4, which have in total 12 element
We can reshape it, but must have the same elements inside
"""

reshaped = A.reshape(2,6)
print(reshaped)

# MAtrix operations

B = np.array([
    [12,11,10,9],
    [8,7,6,5],
    [4,3,2,1]
])

result_add = np.add(A,B)
print(result_add)

result_dot = np.dot(A,B.T)
print(result_dot)

result_transpose = B.T
print(result_transpose)
# One dimensional array
one_d_array = [1,2,3,4,5,6,7,8,9,10]

# Multidimensional Array
two_d_array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(two_d_array[1][2]) # we can accesed the 1 row column 2

three_d_array = [
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
]
"""
When we try to get a specific element from the arry, the first number is which array is taking
the second is the row and the third one is the column
"""
print(three_d_array[1][1][1])

# Dynamic arrays

dynamic_array = []
dynamic_array.append(1)
dynamic_array.append(2)

print(dynamic_array)

# Associative arrays

associative_arrays = {
    "name":"Santiago",
    "lastName":"Aristizabal",
    "Age":"24"
}

print(associative_arrays["name"])

# Sparse Arrays

sparse_array = {
    0:1,
    50:13,
    123:5
}

print(sparse_array)

# Jagged array

jagged_array = [
    [1,2,3],
    [4,5],
    [6,7,8,9]
]
print(jagged_array)
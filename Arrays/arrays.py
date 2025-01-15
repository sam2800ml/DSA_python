# Creating an array 
array = [1,2,3,4,5,6]

#accesing the second element
second_element = print(f"Second element in the array: {array[1]}")

#Modifying elements in a list
"""
In this example we modify the 6th element on the list we change the 6 for the 10
"""
array[5] = 10

print(f"Changing an element: {array}")

array.append(7)

print(f"Appending a number to the array: {array}")

array.extend([11,12])

print(f"extending the array: {array}")

# Removing an element
array.remove(5)
print(f"Removing the number element: {array}")

# Slicing a list
sub_list = array[1:4]
print(f"Creating a new array with index 1:4 from old one: {sub_list}")

for element in array:
    print(element) # we can print each element from the array individually
    print(len(array))


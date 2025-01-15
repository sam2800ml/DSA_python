# Arrays

An array is a fundamental data structure, is used to store a collection of elements, tipically of the same type, they can be accessed using the index, which represents the position within the array.
>
in python we use the list as a form of array, which each element have their own index, provides a more efficient way to store homogeneous data.
they are typically zero-indexed.
>
Arrays support numerous operations, we can append element, extending the array with another array, removing elements
>
When an array needs to resize, a new block of memory is allocated, and the existing elements are copy from one side to another, but this takes time in the process and can lead to inefficiencies.

## Array Operations

We can trasvers an array we can acces each element of the array fo rvarious operations, we can print them, modify them.
>
We can also check the length of the array to know how many items do we have in the array

## Types of array
Depending on the problem that we are working we can use different type of dimensionality of the array.
>
we can have the following:
- One dimensional: Is the simplest form of array can be visualized as a list of elements, is the type linear, and each element are accesed based on their index

- Multidimensional: these are arrays of arrays, they can be of two elements or even more

- Dynamic: This vary from the static arrays, becuase can dynamically resize depending the elements that are added or removed

- Associative(Dictionaries): This uses key-value pairs for indexing, allowing data retrieval and storage

- Sparse: are specially designed to handle data that contains a majority of default values (typically zeros)

- Jagged: Are multidimentional arrays where rows have different lengths, unlike tradiotional list, these can have different list, if different lengths

## Applications in Matrix Operations
for matrix operations we use numpy, numpy is a library in python which helps us to being able to operate them, to create the arrays, and to do multiple procces with it, is the main one used ini a lot of the process



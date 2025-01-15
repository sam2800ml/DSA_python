class Node: # This is our node class
    def __init__(self, data): # here we define what are we going to have
        self.data = data # stores the value of the node
        self.next = None # in this case, this will be the direction of the next data

class linked_list:  # class linked list
    def __init__(self):
        self.head = None # this is going to be our pointer, is the reference to the first node created
       
    def append(self, data): # we create the append this is how we are gonna add everything to the list
        new_node = Node(data) # we create the new node
        if self.head is None: # in the first run we are going to update the pointer that we are going to be  using 
            self.head = new_node # The first number will be our pointer
        else: # in the second iteration we are going to be skipping out pointer
            current = self.head # 
            while current.next:
                current = current.next
            current.next = new_node


# Create a linked list
ll = linked_list()

# Append elements
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
# Traverse the list to print elements
current = ll.head
print(current.data)
while current:
    print(current.data, end=" -> ")
    current = current.next
# Output: 1 -> 2 -> 3 ->

            

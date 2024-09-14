# Queue can also work as LIFO (Last In, First Out)
# put() is used to push the element into the queue
# get() is used to take out the last element from the queue

# Initialize the LifoQueue from the queue module
from queue import LifoQueue

# There are various methods available for this module:
# 1. maxsize():- returns the max size of the queue
# 2. empty():- returns True if the queue is empty, else False
# 3. full():- returns True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default),
#    then full() never returns True.
# 4. get():- Remove and return an item from the queue. If the queue is empty, wait until an item is available.
# 5. get_nowait():- Return an item if one is immediately available, else raise QueueEmpty.
# 6. put(item):- Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# 7. put_nowait(item):- Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# 8. qsize():- Return the number of items in the queue.

stack = LifoQueue(maxsize=3)  # Define Stack with the maxsize = 3

# qsize() shows the number of elements
print(stack.qsize())

# Inserting the elements in the stack
stack.put(3)
stack.put(4)
stack.put(5)

# get() to get the last element from the queue (LIFO behavior)
print(stack.get())  # This will print 5, the last inserted element


# check the stack is empty or not empty() 

print("Is stack is empty? :", stack.empty())

# check the stack is full or not full()
print("Is stack is full?: ", stack.full())

# check how many elements are there
print("how many elements are there: ", stack.qsize())
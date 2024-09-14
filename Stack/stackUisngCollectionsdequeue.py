# Stack using collections.dequeue

'''
Python stack can be implemented using the deque class from the collections 
module. Deque is preferred over the list in the cases where we need quicker 
append and pop operations from both the ends of the container, 
as deque provides an O(1) time complexity for append and pop operations as 
compared to list which provides O(n) time complexity.
'''

#imported dequeue from collections
from collections import deque

# Initializes stack as dequeue
stack = deque()

# using append() for the stack

stack.append('s')
stack.append('h')
stack.append('i')
stack.append('v')
stack.append('a')
stack.append('n')
stack.append('i')

# using pop() for to pop the last entered element

print(stack.pop())
print(stack.pop())

# using peek/top to check the top element
'''In peek/top doesn't work'''
#print(stack.top())

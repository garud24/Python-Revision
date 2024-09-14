## Stack using List
'''
The Pyton build in List is used to implement the Stack. List append() is used to add element at the top 
and pop() is used to remove the element in the LIFO order.
'''

## The disadvantage of it is:

'''
As the list grows, the speed is slowed.
The items in the list are stored next to each other in memory, 
if the stack grows bigger than the block of memory that currently holds it, 
then Python needs to do some memory allocations. 
This can lead to some append() calls taking much longer than other ones.
'''

# Define stack as a List
stack = []

#Implement the append() to push the element at the top of the stack

stack.append('H')
stack.append('i')
stack.append('m')
stack.append('a')
stack.append('n')
stack.append('s')
stack.append('h')
stack.append('u')

# pop() is used to pop the element from the top

print(stack.pop())
print(stack.pop())

#Check the stack how many elements are there
print(stack)

# Checking the peek()/top()
# The top and peek doesn't used in the list datastructure




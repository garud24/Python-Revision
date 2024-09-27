'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


'''

from queue import LifoQueue

class MinStack:

    def __init__(self):
        self.stack = LifoQueue()
        self.min_stack = LifoQueue()

    def push(self, val: int) -> None:
        self.stack.put(val)
        # Push the value to min_stack if it's the smallest so far
        if self.min_stack.empty() or val <= self.min_stack.queue[-1]:
            self.min_stack.put(val)

    def pop(self) -> int:
        if self.stack.empty():
            raise IndexError("pop from empty stack")

        top_val = self.stack.get()

        # If the popped value is the current minimum, pop from the min_stack as well
        if top_val == self.min_stack.queue[-1]:
            self.min_stack.get()

        return top_val

    def top(self) -> int:
        if self.stack.empty():
            raise IndexError("top from empty stack")
        
        return self.stack.queue[-1]

    def getMin(self) -> int:
        if self.min_stack.empty():
            raise IndexError("getMin from empty stack")
        
        return self.min_stack.queue[-1]


# Example usage:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         return self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)
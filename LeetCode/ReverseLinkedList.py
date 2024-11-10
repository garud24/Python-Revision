'''
Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ReverseList:

    def __init__(self):
        self.head = None

# function to append the node at the end of the linked list
    def appendAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node = self.head
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

# function to print the linked list
    def printList(self):
        if self.head is None:
            print("The list is empty")
        curr = self.head 
        while curr:
            print(curr.data,end=" -> ")
            curr = curr.next
        print("None")

# function to rever the linked list
    def ReverseList(self):
        curr = self.head
        prev = None

        while curr is not None:
            Next = curr.next
            curr.next = prev
            
            prev = curr
            curr = Next 
        self.head = prev


list1 = ReverseList()
list1.appendAtEnd(1)
list1.appendAtEnd(2)
list1.appendAtEnd(4)

list1.printList()

list1.ReverseList()
list1.printList()

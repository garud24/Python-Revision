'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        # Merge two lists
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # Attach remaining nodes
        curr.next = list1 if list1 else list2

        return dummy.next

class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node to the end
    def appendAtEnd(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print the linked list
    def printList(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example Usage
# Creating two sorted linked lists:
list1 = LinkedList()
list1.appendAtEnd(1)
list1.appendAtEnd(2)
list1.appendAtEnd(4)

list2 = LinkedList()
list2.appendAtEnd(1)
list2.appendAtEnd(3)
list2.appendAtEnd(4)

# Merging the lists
solution = Solution()
merged_head = solution.mergeTwoLists(list1.head, list2.head)

# Printing the result
merged_list = LinkedList()
merged_list.head = merged_head
print("Merged List:")
merged_list.printList()

        
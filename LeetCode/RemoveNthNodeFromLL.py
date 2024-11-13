'''
Remove the nth node from the Linked List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Remove_N_Node_Linked_List:

    def __init__(self):
        self.head = None

    # function to append at end of the list
    def append_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node = self.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # function to display the linked list
    def display_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("None")

    # function to remove the nth node from the list {This is the wrong solution}
    # def removeNthFromEnd(self,n):
    #     prev, Next = self.head, self.head 

    #     if prev.data == n:
    #         self.head = prev.next
    #         return self.head
    #     else:
    #         Next = Next.next
    #         while Next:
    #             if Next.data == n:
    #                 prev.next = Next.next
    #                 return
    #             Next = Next.next
    #             prev = prev.next  

    # function to remove the Nth node from the end of the list
    def removeNthFromEnd(self, n):
        dummy = Node(0)
        dummy.next = self.head

        left, right = dummy, self.head     

        while n > 0 and right:
            right = right.next
            n -=1

        while right:
            left = left.next 
            right = right.next

        temp = left.next.next
        left.next = temp



ll = Remove_N_Node_Linked_List()
ll.append_at_end(1)
ll.append_at_end(2)
ll.append_at_end(3)
ll.append_at_end(4)
ll.append_at_end(5)
#ll.append_at_end(28)


ll.display_linked_list()

ll.removeNthFromEnd(2)
ll.display_linked_list()
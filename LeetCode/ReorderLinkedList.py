class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Reorder_linked_list:
    def __init__(self):
        self.head = None

    def add_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node = self.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")

        curr = self.head 
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")

    def reverse_linked_list(self, curr_node):
        curr = curr_node
        prev = None

        while curr:
            Next = curr.next
            curr.next = prev

            prev = curr
            curr = Next 
        curr_node = prev
        return curr_node

    def reorder(self):

        slow, fast = self.head, self.head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse_list = self.reverse_linked_list(slow.next)
        slow.next = None
        

        first = self.head 
        second = reverse_list

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
     
           


ll = Reorder_linked_list()
ll.add_at_end(1)
ll.add_at_end(2)              
ll.add_at_end(3)              
ll.add_at_end(4)              
ll.add_at_end(5)
#ll.print_linked_list()      

ll.reorder()

ll.print_linked_list()


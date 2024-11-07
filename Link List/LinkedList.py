# A simple linked list example 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # Insert Node at begninning 
    def insert_at_beginning(self,data):
        # If head is pointing to None, then point the head to the new node 
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Print Node
    def display(self):
        curr = self.head
        while curr.next is not None:
            print(curr.data)
            curr = curr.next
        print(curr.data)   

    # insert at end 
    def insert_at_end(self,data):
        
        new_node = Node(data)
        #print("The value of head", self.head)
        if self.head is None:
            new_node.next = self.head
            self.head =  new_node 
            print("True")
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
                #print("Inside the function Insert at end: ",curr.data), for debugging purpose
            curr.next = new_node

    # remove a node from the beginning
    def remove_node_at_beginning(self):
        if self.head is None:
            print("The Linked List is empty")
            return
        else:
            curr = self.head.next
            self.head = curr

    # remove a node from the end
    def remove_node_at_end(self):
        if self.head is None:
            print("The linked List is empty")   
            return
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
                print(curr.data)    
            temp = curr.next
            curr.next = None
            print("The removed node is: ", temp.data)
             



llist = SinglyLinkedList()
llist.insert_at_beginning(2)
llist.insert_at_beginning(1)
llist.insert_at_beginning(0)

print("Demonstrating insert at beginning: \n")
llist.display()

llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)


print("Demonstrating insert at end: \n")
llist.display()

print("Demonstrating remove at beginning: \n")
llist.remove_node_at_beginning()
llist.display()

print("\n")
llist.remove_node_at_beginning()
llist.display()

print("Demonstrating remove at end: \n")
llist.remove_node_at_end()
llist.display()


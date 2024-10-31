'''
The Singly Linked List performs the following operations:

insert_at_beginning adds a node to the beginning of the list.
insert_at_end adds a node to the end.
display traverses the list and prints each element.
delete_node removes a node by its value.

'''


# Class Node implementation
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Singly Linked List implementation

class LinkedList:


    def __init__(self):
        self.head = None

    # Method to add the node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add the node at the last of the linked list
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Display the link list
    def display(self):
        current = self.head 
        while current:
            print(current.data, end = "->")
            current = current.next
        print("None")

def main():
    ll = LinkedList()
    while True:
        print("\nChoose an operation:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Display the list")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = input("Enter the data to insert at the beginning: ")
            ll.insert_at_beginning(int(data))
            print(f"Inserted {data} at the beginning of the list.")
        
        elif choice == '2':
            data = input("Enter the data to insert at the end: ")
            ll.insert_at_end(int(data))
            print(f"Inserted {data} at the end of the list.")

        elif choice == '3':
            print("Current Linked List:")
            ll.display()

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()   

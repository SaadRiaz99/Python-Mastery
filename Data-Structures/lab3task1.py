
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the tail
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Insert a node at the head
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Display the full list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Delete a node by subject name
    def delete_by_name(self, name):
        current = self.head

        if current is not None and current.data == name:
            self.head = current.next
            return True

        previous = None

        while current is not None:
            if current.data == name:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    # Search for a subject and report its position
    def search(self, name):
        current = self.head
        hops = 0

        while current is not None:
            if current.data == name:
                print(f"{name} found at position {hops + 1}")
                print(f"Number of hops from head: {hops}")
                return

            current = current.next
            hops += 1

        print(f"{name} was not found in the list.")


# # TASK 1: Create a list of five subjects
# print("Saad Bin Riaz")
# print("BAI-25F-035")
subjects = LinkedList()

# subjects.insert_at_tail("Programming")
# subjects.insert_at_tail("Mathematics")
# subjects.insert_at_tail("Physics")
# subjects.insert_at_tail("Database Systems")
# subjects.insert_at_tail("English")

# print("TASK 1: Original List")
# subjects.display()


# TASK 2: Insert at head and tail
# print("Saad Bin Riaz")
# print("BAI-25F-035")
# subjects.insert_at_head("Computer Networks")
# print("\nTASK 2: After Insertion at Head")
# subjects.display()

# subjects.insert_at_tail("Artificial Intelligence")
# print("After Insertion at Tail")
# subjects.display()


# TASK 3: Delete a subject by name
print("Saad Bin Riaz")
print("BAI-25F-035")
print("\nTASK 3: Before Deletion")
subjects.display()

subjects.delete_by_name("Physics")

print("After Deletion of Physics")
subjects.display()


# TASK 4: Search for a subject
# print("Saad Bin Riaz")
# print("BAI-25F-035")
# print("\nTASK 4: Search Operation")
# subjects.search("Database Systems")

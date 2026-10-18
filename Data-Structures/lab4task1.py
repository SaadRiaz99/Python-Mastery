class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Task 1

subjects = DoublyLinkedList()

subjects.insert_at_tail("Python")
subjects.insert_at_tail("Mathematics")
subjects.insert_at_tail("Database")
subjects.insert_at_tail("Networking")
subjects.insert_at_tail("Operating Systems")

print("Forward:")
subjects.display_forward()

print("Backward:")
subjects.display_backward()
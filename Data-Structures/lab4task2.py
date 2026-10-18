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

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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


# Task 2
print("Saad Bin Riaz")
print("BAI-25F-035")
subjects = DoublyLinkedList()

for subject in ["Python", "Mathematics", "Database", "Networking", "Operating Systems"]:
    subjects.insert_at_tail(subject)

print("Initial list:")
print("Forward:")
subjects.display_forward()
print("Backward:")
subjects.display_backward()

print("\nAfter inserting 'Physics' at the head:")
subjects.insert_at_head("Physics")
print("Forward:")
subjects.display_forward()
print("Backward:")
subjects.display_backward()

print("\nAfter inserting 'Statistics' at the tail:")
subjects.insert_at_tail("Statistics")
print("Forward:")
subjects.display_forward()
print("Backward:")
subjects.display_backward()

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

    def delete_node(self, node):
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None

    def find_by_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def forward_list(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

    def backward_list(self):
        items = []
        current = self.tail
        while current:
            items.append(current.data)
            current = current.prev
        return items

    def display_forward(self):
        print(" <-> ".join(self.forward_list()) or "None")

    def display_backward(self):
        print(" <-> ".join(self.backward_list()) or "None")

    def is_mirror(self):
        return self.forward_list() == self.backward_list()[::-1]


# Task 3

subjects = DoublyLinkedList()

for subject in ["Python", "Mathematics", "Database", "Networking", "Operating Systems"]:
    subjects.insert_at_tail(subject)

print("Initial list:")
print("Forward:")
subjects.display_forward()
print("Backward:")
subjects.display_backward()

print("\nAfter deleting 'Database' from the middle:")
subjects.delete_node(subjects.find_by_data("Database"))
print("Forward:")
subjects.display_forward()
print("Backward:")
subjects.display_backward()
print("Forward and backward are mirror images:", subjects.is_mirror())

print("\nAfter deleting the head 'Python':")
subjects.delete_node(subjects.head)
print("Forward:")
subjects.display_forward()
print("Backward:")
subjects.display_backward()
print("Forward and backward are mirror images:", subjects.is_mirror())

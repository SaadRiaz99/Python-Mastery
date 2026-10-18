class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


# Task 4
print("Saad Bin Riaz")
print("BAI-25F-035")
subjects = CircularLinkedList()

for subject in ["Python", "Mathematics", "Database", "Networking"]:
    subjects.insert_at_tail(subject)

print("Circular list:")
subjects.display()

print("10 consecutive nodes starting at head (wraps around):")
current = subjects.head
for _ in range(10):
    print(current.data, end=" -> ")
    current = current.next
print()

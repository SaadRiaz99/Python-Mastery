print("Saad Bin Riaz")
print("BAI-25F-035")

print("\nTask 5(a): Deleting a node you already hold a reference to")
print(
    "In a doubly linked list, the node object itself stores a 'prev' pointer, "
    "so if you already hold a reference to the node you can immediately find "
    "its predecessor and relink prev.next and next.prev in O(1) time without "
    "searching. In a singly linked list, a node only knows its successor, so "
    "even with a reference to the node you must traverse from the head to find "
    "the previous node (O(n)) before you can delete it. The extra backward "
    "link removes that costly search."
)

print("\nTask 5(b): Real-world fit for a circular linked list")
print(
    "A natural fit is round-robin scheduling in operating systems: ready "
    "processes are kept in a circular list, and the CPU cycles through them "
    "one after another, wrapping back to the first process after the last. "
    "The circular structure means the scheduler never hits a null end and can "
    "keep cycling fairly through every process with a simple next pointer."
)

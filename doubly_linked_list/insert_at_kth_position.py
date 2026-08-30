class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3


# Head and Tail
head = node1
tail = node4


# Insert at Kth Position
def insert_at_k(head, data, k):

    new_node = Node(data)

    # Case 1: Insert at beginning
    if k == 1:
        new_node.next = head

        if head is not None:
            head.prev = new_node

        return new_node

    current = head

    # Move to the node before position k
    for i in range(k - 2):
        current = current.next

    # Connect new node to next node
    new_node.next = current.next

    # Connect new node to previous node
    new_node.prev = current

    # Connect previous node to new node
    current.next = new_node

    # Connect next node back to new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    return head


# Insert 25 at position 3
head = insert_at_k(head, 25, 3)


# Forward Traversal
print("Forward:")

current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")


# Find tail after insertion
tail = head

while tail.next is not None:
    tail = tail.next


# Backward Traversal
print("Backward:")

current = tail

while current is not None:
    print(current.data, end=" <-> ")
    current = current.prev

print("None")
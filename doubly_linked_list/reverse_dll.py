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


# Head
head = node1


# Reverse Doubly Linked List
def reverse_dll(head):

    current = head
    new_head = None

    while current is not None:

        # Swap prev and next
        current.prev, current.next = current.next, current.prev

        # Current becomes the new head
        new_head = current

        # Move to the next node
        current = current.prev

    return new_head


# Reverse the list
head = reverse_dll(head)


# Forward traversal after reversal
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")
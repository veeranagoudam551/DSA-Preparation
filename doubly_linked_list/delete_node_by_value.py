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

head = node1


def delete_by_value(head, value):

    if head is None:
        return None

    current = head

    # Find the node
    while current is not None and current.data != value:
        current = current.next

    # Value not found
    if current is None:
        return head

    # If deleting head
    if current.prev is None:
        head = current.next

        if head is not None:
            head.prev = None

        return head

    # Connect previous node to next node
    current.prev.next = current.next

    # Connect next node to previous node
    if current.next is not None:
        current.next.prev = current.prev

    return head


# Delete node containing 30
head = delete_by_value(head, 30)


# Forward traversal
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")
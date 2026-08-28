class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head
head = node1


def insert_at_k_position(head, data, k):

    # Create new node
    new_node = Node(data)

    # Insert at beginning
    if k == 1:
        new_node.next = head
        return new_node

    current = head

    # Move to position k-1
    for i in range(k - 2):
        current = current.next

    # Insert new node
    new_node.next = current.next
    current.next = new_node

    return head
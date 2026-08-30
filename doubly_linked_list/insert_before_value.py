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


# Insert before a particular value
def insert_before_value(head, data, value):

    new_node = Node(data)

    # If list is empty
    if head is None:
        return head

    # If value is at head
    if head.data == value:
        new_node.next = head
        head.prev = new_node
        return new_node

    current = head

    # Find the value
    while current is not None and current.data != value:
        current = current.next

    # Value not found
    if current is None:
        return head

    # Insert before current
    new_node.prev = current.prev
    new_node.next = current

    current.prev.next = new_node
    current.prev = new_node

    return head


# Insert 25 before 30
head = insert_before_value(head, 25, 30)


# Forward traversal
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")
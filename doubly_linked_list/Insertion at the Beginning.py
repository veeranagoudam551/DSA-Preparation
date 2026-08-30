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


# Insert at beginning
def insert_at_head(head, data):

    new_node = Node(data)

    new_node.next = head

    if head is not None:
        head.prev = new_node

    head = new_node

    return head


head = insert_at_head(head, 5)


# Forward traversal
current = head

while current is not None:
    print(current.data, end=" ⇄ ")
    current = current.next

print("None")
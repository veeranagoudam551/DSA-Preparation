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

# Head and tail
head = node1
tail = node4


# Insert at end
def insert_at_end(tail, data):

    new_node = Node(data)

    new_node.prev = tail
    tail.next = new_node

    tail = new_node

    return tail


tail = insert_at_end(tail, 50)


# Forward traversal
current = head

while current is not None:
    print(current.data, end=" ⇄ ")
    current = current.next

print("None")
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
tail = node4


# Delete tail
def delete_tail(tail):

    if tail is None:
        return None

    tail = tail.prev

    if tail is not None:
        tail.next = None

    return tail


tail = delete_tail(tail)


# Forward traversal
current = head

while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")